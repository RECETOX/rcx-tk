import itertools
from collections.abc import Callable
import numpy as np
import pandas as pd
from rcx_tk.io import read_file
from rcx_tk.io import save_dataframe_as_tsv
from rcx_tk.utils import concat_str


def process_msdial_file(file_path: str, out_path: str) -> None:
    """Process MSDial output file to group duplicate alignments.

    Args:
        file_path (str): Input file path.
        out_path (str): Output file path.
    """
    df = read_file(file_path, header=4, index_col=0)
    n_samples = get_n_samples(file_path)
    result = process_msdial(df, n_samples)

    with open(file_path) as infile:
        with open(out_path, mode="w+") as outfile:
            [outfile.write(infile.readline()) for _ in range(4)]

    save_dataframe_as_tsv(result, out_path, index=True, mode="a")

def get_n_samples(file_path: str) -> int:
    with open(file_path) as file:
        first = file.readline().strip('\t').split('\t')
    
    n_samples = len(list(filter(lambda x: x != 'NA', first))[1:-1])
    return n_samples


def process_msdial(df: pd.DataFrame, n_samples: int, metadata_cols: int = 27, index_col: str = "Alignment ID") -> pd.DataFrame:
    """Function to process a DataFrame of MSDial results to group duplicate alignments.

    Args:
        df (pd.DataFrame): Dataframe with MSDial results.
        metadata_cols (int, optional): Number of columns containing data prior to feature abundances. Defaults to 28.
        index_col (str, optional): Column to denote the index. Defaults to "Alignment ID".

    Returns:
        pd.DataFrame: DataFrame with clustered alignment ids.
    """
    data_matrix = df.loc[:, df.columns[metadata_cols:n_samples+metadata_cols]]

    all_duplicates = find_all_duplicates(data_matrix)
    all_duplicates_idx = union(all_duplicates)

    alignments_with_duplicates = df.loc[all_duplicates_idx]

    metadata_columns = list(df.columns[:metadata_cols])
    mean_columns = metadata_columns[:3]
    concat_columns = metadata_columns[3:]
    abundance_columns = list(df.columns[metadata_cols:])

    clusters = refine(find_clusters(all_duplicates), df[metadata_columns])

    aggregate_functions = aggregations(mean_columns, concat_columns, abundance_columns)

    results = {
        concat_str(cluster): alignments_with_duplicates.loc[cluster].agg(aggregate_functions) for cluster in clusters
    }

    summary_df = pd.DataFrame.from_dict(results, orient="index", columns=df.columns)
    summary_df.index.name = index_col
    df.drop(all_duplicates_idx, inplace=True)
    everything = pd.concat([df, summary_df])
    return everything

def refine(clusters : list[pd.Index], metadata: pd.DataFrame) -> list[pd.Index]:
    refined_clusters: list[pd.Index] = []
    for cluster in clusters:
        cluster_metadata = metadata.loc[cluster].sort_values(by='Quant mass')
        mz_tols = 10e-06 * cluster_metadata['Quant mass']
        cluster_metadata['subcluster'] = np.cumsum(cluster_metadata['Quant mass'].diff().fillna(0).abs() > mz_tols)
        subclusters = list(cluster_metadata.groupby(by='subcluster').groups.values())
        refined_clusters.extend(subclusters)

    return refined_clusters

def aggregations(
    mean_columns: list[str], concat_columns: list[str], abundance_columns: list[str]
) -> dict[str, Callable]:
    """Generate aggregation functions based on column types.

    Args:
        mean_columns (list[str]): List of columns to aggregate using mean.
        concat_columns (list[str]): List of columns to aggregate using concatenation.
        abundance_columns (list[str]): List of columns to aggregate using max.

    Returns:
        dict[str, function]: Dictionary with functions to use for pd.aggregate
    """
    aggregate_functions = {}

    for col in mean_columns:
        aggregate_functions[col] = np.mean

    for col in concat_columns:
        aggregate_functions[col] = concat_str

    for col in abundance_columns:
        aggregate_functions[col] = np.max
    return aggregate_functions


def find_clusters(all_duplicates: list[pd.Index]) -> list[pd.Index]:
    """Transitive merging of all duplicate indices into groups, where groups are merged if there is any overlap.

    Args:
        all_duplicates (list[pd.Index]): List of all duplicate indices.

    Returns:
        list[pd.Index]: Clusters of connected duplicates.
    """
    clusters: list[pd.Index] = []
    while all_duplicates:
        current = all_duplicates.pop()
        
        matches = [
            cluster_idx
            for cluster_idx, cluster in enumerate(clusters)
            if current.isin(cluster).any()
        ]
        
        if len(matches) == 0:
            clusters.append(current)
        elif len(matches) == 1:
            match = matches[0]
            if clusters[match].equals(current):
                continue
            else:
                clusters[match] = clusters[match].union(current)
        else:
            merging = [clusters[match] for match in matches]
            merging.append(current)
            clusters[matches[0]] = union(merging)
            del clusters[matches[1]]

    return clusters


def union(all_duplicates: list[pd.Index]) -> pd.Index:
    """Function to combine list of indices to union index.

    Args:
        all_duplicates (list[pd.Index]): All indices to combine.

    Returns:
        pd.Index: Union of all indices.
    """
    all_duplicates_idx = all_duplicates[0]
    for idx in all_duplicates:
        all_duplicates_idx = all_duplicates_idx.union(idx)
    return all_duplicates_idx


def find_all_duplicates(data_matrix: pd.DataFrame) -> list[pd.Index]:
    """Get index of any duplicate values in any column.

    Args:
        data_matrix (pd.DataFrame): DataFrame to check column-by-column for duplicate values.

    Returns:
        list[pd.Index]: All indexes of duplicates.
    """
    duplicates = {}
    for col_idx in range(len(data_matrix.columns)):
        col = data_matrix.iloc[:, col_idx].astype(float)
        col = col.loc[col > 0]
        groups = col.drop(col.drop_duplicates(keep=False).index).groupby(col)
        duplicates[col.name] = [g.index for val, g in groups]

    all_duplicates = list(itertools.chain(*[val for key, val in duplicates.items()]))
    return all_duplicates
