import os
from pathlib import Path
from typing import Final
import pandas as pd
import pytest
from rcx_tk.io import read_file
from rcx_tk.io import save_dataframe_as_tsv

__location__: Final[Path] = Path(__file__).parent.resolve()


@pytest.mark.parametrize(
    "file_name",
    [
        "batch_specification1.csv",
        "batch_specification1.xlsx",
        "batch_specification1.txt",
    ],
)
def test_read_file(file_name: str, dataframe: pd.DataFrame):
    """Test importing the metadata file into pandas dataframe.

    Args:
        file_name (str): The path to the input data.
        dataframe (pd.DataFrame): Dataframe containing the metadata.
    """
    file_path = __location__.joinpath("test_data", file_name)
    # file_path = os.path.join("tests", "test_data", file_name)
    actual = read_file(str(file_path))
    # assert
    assert actual.equals(dataframe)


def test_read_file_error(dataframe: pd.DataFrame):
    """Test throwing a value error if incorrect file format is supplied.

    Args:
        dataframe (pd.DataFrame): Dataframe containing the metadata.
    """
    file_path = os.path.join("tests", "test_data", "batch_specification1.prn")
    with pytest.raises(
        ValueError,
        match=r"Unsupported file format. Please provide a CSV, Excel, or TSV file.",
    ):
        read_file(file_path)


def test_save_dataframe_as_tsv(dataframe: pd.DataFrame, tmp_path: str):
    """Test saving the dataframe in tsv format.

    Args:
        dataframe (pd.DataFrame): The metadata dataframe.
        tmp_path (str): A path where the .TSV will be exported.
    """
    out_path = os.path.join(tmp_path, "batch_specification1.tsv")

    save_dataframe_as_tsv(dataframe, out_path)
    actual = pd.read_csv(out_path, sep="\t")
    assert actual.equals(dataframe)


def test_read_save_dataframe_as_tsv_error(dataframe: pd.DataFrame, tmp_path: str):
    """Test throwing a value error if provided <fileName> is of different format than TSV.

    Args:
        dataframe (pd.DataFrame): The metadata dataframe.
        tmp_path (str): A path where the .TSV will be exported.
    """
    out_path = os.path.join(tmp_path, "batch_specification1.prn")
    with pytest.raises(ValueError, match=r"Unsupported file format. Please point to a TSV file."):
        save_dataframe_as_tsv(dataframe, out_path)
