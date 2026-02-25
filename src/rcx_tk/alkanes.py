import pandas as pd
from rcx_tk.io import read_file
from rcx_tk.io import save_dataframe_as_tsv


def process_alkane_file(file_path: str, out_path: str) -> None:
    """Processes an alkane file, keeping and renaming specific columns.

    Args:
        file_path (str): A path to the alkane file.
        out_path (str): A path where processed alkane file is exported.
    """
    df = read_file(file_path)
    df = process_alkanes(df)
    save_dataframe_as_tsv(df, out_path)


def process_alkanes(df: pd.DataFrame, columns_to_keep: list[str] = {"Carbon number": "carbon_number", "RT (min)": "rt"}) -> pd.DataFrame:
    """Process dataframe with alkanes to fit the msdial format.

    Args:
        df (pd.DataFrame): Alkanes in MSDial format.
        columns_to_keep (list[str]): List of columns to keep. Default for MSDial files.

    Returns:
        pd.DataFrame: Transformed alkane file dataframe in format used at RCX.
    """
    df.columns = df.columns.str.strip()
    df = df.rename(columns=columns_to_keep)
    return df
