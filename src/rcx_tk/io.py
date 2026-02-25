import os
import pandas as pd


def read_file(file_path: str) -> pd.DataFrame:
    """Imports the metadata file to pandas dataframe.

    Args:
        file_path (str): The path to the input data.

    Raises:
        ValueError: Error if any file format except for csv, xls, xlsx, txt or tsv is provided.

    Returns:
        pd.DataFrame: Dataframe containing the metadata.
    """
    file_extension = os.path.splitext(file_path)[1].lower()
    if file_extension == ".csv":
        return pd.read_csv(file_path, encoding="UTF-8")
    elif file_extension in [".xls", ".xlsx"]:
        return pd.read_excel(file_path)
    elif file_extension in [".tsv", ".txt"]:
        return pd.read_csv(file_path, sep="\t")
    else:
        raise ValueError("Unsupported file format. Please provide a CSV, Excel, or TSV file.")


def save_dataframe_as_tsv(df: pd.DataFrame, file_path: str, header: bool = True, index: bool = False) -> None:
    """Saves the dataframe as a TSV file.

    Args:
        df (pd.DataFrame): The metadata dataframe.
        file_path (str): A path where the .TSV will be exported, containing the <fileName>.TSV.

    Raises:
        ValueError: Error if provided <fileName> is of a different format than TSV.
    """
    if os.path.splitext(file_path)[1] != ".tsv":
        raise ValueError("Unsupported file format. Please point to a TSV file.")
    df.to_csv(file_path, sep="\t", index=index, header=header)
