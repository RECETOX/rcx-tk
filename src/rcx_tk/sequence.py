import re
from typing import Tuple
import pandas as pd
from numpy import int64
from rcx_tk.io import read_file
from rcx_tk.io import save_dataframe_as_tsv
from rcx_tk.utils import replace_spaces
from rcx_tk.utils import validate_filename


def process_sequence_file(file_path: str, out_path: str) -> None:
    """Processes a metadata file, keeping and renaming specific columns.

    Args:
        file_path (str): A path to the metadata file.
        out_path (str): A path where processed metadata dataframe is exported.
    """
    df = read_file(file_path)
    df = process_sequence(df)
    save_dataframe_as_tsv(df, out_path)


def process_sequence(df: pd.DataFrame) -> pd.DataFrame:
    """Processes the metadata dataframe.

    Args:
        df (pd.DataFrame): The metadata dataframe.

    Returns:
        pd.DataFrame: A metadata dataframe with rearranged and newly derived columns.
    """
    df = rearrange_columns(df)
    validate_filenames_column(df)
    validate_injection_order(df)
    df["sampleName"] = df["File name"].apply(replace_spaces)
    df = derive_additional_metadata(df)
    df = cleanup(df)
    return df


def cleanup(df: pd.DataFrame) -> pd.DataFrame:
    """Removes the file Name column and moves the sampleName col.

    Args:
        df (pd.DataFrame): The metadata dataframe.

    Returns:
        pd.DataFrame: The processed dataframe.
    """
    df = df.drop("File name", axis=1)
    column_to_move = df.pop("sampleName")
    df.insert(0, "sampleName", column_to_move)
    return df


def validate_injection_order(df: pd.DataFrame) -> bool:
    """Validates if injectionOrder is of integer type.

    Args:
        df (pd.DataFrame): The metadata dataframe.

    Returns:
        bool: Whether the injectionOrder is integer.
    """
    return df["injectionOrder"].dtypes == int64


def derive_additional_metadata(df: pd.DataFrame) -> pd.DataFrame:
    """Derives additional metadata columns.

    Args:
        df (pd.DataFrame): The metadata dataframe.

    Returns:
        pd.DataFrame: The processed dataframe.
    """
    df["sequenceIdentifier"] = df["File name"].apply(add_sequence_identifier)
    df["subjectIdentifier"] = df["File name"].apply(add_subject_identifier)
    df["localOrder"] = df["File name"].apply(add_local_order)
    return df


def rearrange_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Rearranges the columns.

    Args:
        df (pd.DataFrame): The metadata dataframe.

    Returns:
        pd.DataFrame: The processed dataframe.
    """
    columns_to_keep = ["File name", "Type", "Class ID", "Batch", "Analytical order"]

    df = df[list(columns_to_keep)]

    df = df.rename(
        columns={"Type": "sampleType", "Class ID": "class", "Batch": "batch", "Analytical order": "injectionOrder"}
    )

    return df


def validate_filenames_column(df: pd.DataFrame) -> None:
    """Validates the file names.

    Args:
        df (pd.DataFrame): A dataframe to process.

    Raises:
        ValueError: An error if there is any invalid file name.
    """
    if not df["File name"].apply(validate_filename).all():
        raise ValueError("Invalid File name.")


def add_local_order(file_name: str) -> int:
    """Returns the localOrder value, i.e. the last n-digits after the last underscore.

    Args:
        file_name (str): The filename.

    Returns:
        int: The localOrder value.
    """
    _, b = separate_filename(file_name)
    return int(b)


def add_sequence_identifier(file_name: str) -> str:
    """Returns the sequenceIdentifier value, i.e. everything before last _[digits].

    Args:
        file_name (str): The filename.

    Returns:
        str: The sequenceIdentifier value.
    """
    a, _ = separate_filename(file_name)
    a = a.rstrip("_")
    a = a.strip()
    return a


def separate_filename(file_name: str) -> Tuple[str, str]:
    """Split a filename into the non-numeric prefix and trailing numeric suffix.

    Args:
        file_name (str): The filename.

    Returns:
        Tuple[str, str]: Splitted file_name.
    """
    a, b = re.findall(r"^(.*\D)(\d+)$", file_name)[0]
    return (a, b)


def add_subject_identifier(file_name: str) -> str:
    """Returns the subjectIdentifier value, i.e. everything between [digit_] and [_digit].

    Args:
        file_name (str): The filename.

    Returns:
        str: The subjectIdentifier value.
    """
    _, b, _ = re.findall(r"^(\d+_)(.*?)(_\d+)$", file_name)[0]
    b = b.strip()
    return b
