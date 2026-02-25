import itertools
import numpy as np
import pandas as pd
from rcx_tk.io import read_file
from rcx_tk.io import save_dataframe_as_tsv
from rcx_tk.utils import concat_str

skip_rows = 3
metadata_cols = 28
index_col = "Alignment ID"


def process_msdial_file(file_path: str, out_path: str) -> None:
    df = read_file(file_path)
    result = process_msdial(df)
    save_dataframe_as_tsv(result, out_path, header=False, index=True)


def process_msdial(df: pd.DataFrame, skip_rows: int = 3, metadata_cols: int = 28, index_col: str = "Alignment ID"):
    df.columns = df.iloc[skip_rows]
    df.set_index(index_col, inplace=True, drop=True)
    data_matrix = df.loc[skip_rows:, df.columns[metadata_cols:]]

    all_duplicates = find_all_duplicates(data_matrix)
    all_duplicates_idx = get_index(all_duplicates)

    alignments_with_duplicates = df.loc[all_duplicates_idx]
    df.drop(all_duplicates_idx, inplace=True)

    clusters = find_clusters(all_duplicates)

    metadata_columns = list(df.columns[:metadata_cols])
    mean_columns = metadata_columns[:3]
    concat_columns = metadata_columns[3:]
    abundance_columns = list(df.columns[metadata_cols:])

    aggregate_functions = aggregations(mean_columns, concat_columns, abundance_columns)

    results = {
        concat_str(cluster): alignments_with_duplicates.loc[cluster].agg(aggregate_functions) for cluster in clusters
    }

    summary_df = pd.DataFrame.from_dict(results, orient="index", columns=df.columns)
    summary_df.index.name = index_col
    everything = pd.concat([df, summary_df])
    return everything


def aggregations(mean_columns, concat_columns, abundance_columns):
    aggregate_functions = {}

    for col in mean_columns:
        aggregate_functions[col] = np.mean

    for col in concat_columns:
        aggregate_functions[col] = concat_str

    for col in abundance_columns:
        aggregate_functions[col] = np.max
    return aggregate_functions


def find_clusters(all_duplicates):
    clusters = []
    while all_duplicates:
        current = all_duplicates.pop()
        added = False
        for cluster_idx in range(len(clusters)):
            if any(current.isin(clusters[cluster_idx])):
                clusters[cluster_idx] = clusters[cluster_idx].union(current)
                added = True
                break
        if not added:
            clusters.append(current)
    return clusters


def get_index(all_duplicates):
    all_duplicates_idx = all_duplicates.pop()
    for idx in all_duplicates:
        all_duplicates_idx = all_duplicates_idx.union(idx)
    return all_duplicates_idx


def find_all_duplicates(data_matrix):
    duplicates = {}
    for col_idx in range(len(data_matrix.columns)):
        col = data_matrix.iloc[:, col_idx].astype(float)
        col = col.loc[col > 0]
        groups = col.drop(col.drop_duplicates(keep=False).index).groupby(col)
        duplicates[col.name] = [g.index for val, g in groups]

    all_duplicates = list(itertools.chain(*[val for key, val in duplicates.items()]))
    return all_duplicates
