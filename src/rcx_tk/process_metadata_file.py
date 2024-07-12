import os
import re
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


def save_dataframe_as_tsv(df: pd.DataFrame, file_path: str) -> None:
    """Saves the dataframe as a TSV file.

    Args:
        df (pd.DataFrame): The metadata dataframe.
        file_path (str): A path where the .TSV will be exported, containing the <fileName>.TSV.

    Raises:
        ValueError: Error if provided <fileName> is of a different format than TSV.
    """
    if os.path.splitext(file_path)[1] != ".tsv":
        raise ValueError("Unsupported file format. Please point to a TSV file.")
    df.to_csv(file_path, sep="\t", index=False)


def process_metadata_file(file_path: str, out_path: str) -> None:
    """Processes a metadata file, keeping and renaming specific columns.

    Args:
        file_path (str): A path to the metadata file.
        out_path (str): A path where processed metadata dataframe is exported.
    """
    columns_to_keep = {
        "File name": "sampleName",
        "Type": "sampleType",
        "Class ID": "class",
        "Batch": "batch",
        "Analytical order": "injectionOrder",
    }

    df = read_file(file_path)
    df = df[list(columns_to_keep.keys())].rename(columns=columns_to_keep)
    df["sampleName"] = df["sampleName"].str.replace(" ", "_")
    save_dataframe_as_tsv(df, out_path)


def process_alkane_ri_file(file_path: str, out_path: str) -> None:
    """Processes an alkane file, keeping and renaming specific columns.

    Args:
        file_path (str): A path to the alkane file.
        out_path (str): A path where processed alkane file is exported.
    """
    columns_to_keep = {"Carbon number": "carbon_number", "RT (min)": "rt"}

    df = read_file(file_path)
    df.columns = df.columns.str.strip()
    df = df.rename(columns=columns_to_keep)
    save_dataframe_as_tsv(df, out_path)


def validate_filename(file_name: str) -> bool:
    """Validate a filename.

    Args:
        file_name (str): Filename to validate.

    Returns:
        bool: Validity of the filename.
    """
    def is_not_empty(x: str) -> bool:
        return x != ''

    tokens: list[str] = list(filter(is_not_empty, file_name.split('_')))
    return len(tokens) > 1 and tokens[-1].isdigit()

def add_localOrder(file_name: str) -> int:
    """Returns the localOrder value, i.e. the last n-digits after the last underscore.

    Args:
        file_name (str): The filename.

    Returns:
        int: The localOrder value.
    """
    a, b = re.findall(r'(.*(?:\D|^))(\d+)', file_name)[0]
    return(int(b))

def add_sequenceIdentifier(file_name: str) -> str:
    """Returns the sequenceIdentifier value, i.e. everything before last _[digits].

    Args:
        file_name (str): The filename.

    Returns:
        str: The sequenceIdentifier value.
    """
    a, b = re.findall(r'(.*(?:\D|^))(_\d+)', file_name)[0]
    a = a.strip()
    return(a)
