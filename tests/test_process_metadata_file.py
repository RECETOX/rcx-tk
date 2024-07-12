import os
from pathlib import Path
from typing import Final
import pandas as pd
import pytest
from rcx_tk.process_metadata_file import process_alkane_ri_file
from rcx_tk.process_metadata_file import process_metadata_file
from rcx_tk.process_metadata_file import read_file
from rcx_tk.process_metadata_file import save_dataframe_as_tsv
from rcx_tk.process_metadata_file import validate_filename

__location__: Final[Path] = Path(__file__).parent.resolve()


@pytest.fixture
def dataframe() -> pd.DataFrame:
    """Creates a dataframe corresponding to metadata test file.

    Returns:
        pd.DataFrame: Expected dataframe matching metadata test file.
    """
    path_prefix: Final[str] = (
        "Z:\\000020-Shares\\hram\\MS_omics\\Personal Folders\\COUFALIKOVA Katerina\\ATHLETE\\finalni data zaloha\\batch1-20231121-Katerina Coufalikova\\RAW_profile\\"  # noqa: E501 path prefix is expected in test data to be longer than line limit
    )
    d = {
        "File path": [
            path_prefix + "1_instrumental blank_01.raw",
            path_prefix + "4_Alkane mix_04.raw",
            path_prefix + "6_instrumental blank_06.raw",
            path_prefix + "7_procedural blank_07.raw",
            path_prefix + "8_QC non-dilute_08.raw",
            path_prefix + "11_QC 16_11.raw",
            path_prefix + "12_QC 8_12.raw",
            path_prefix + "15_QC non-dilute_15.raw",
            path_prefix + "18_QC 4 _18.raw",
            path_prefix + "19_QC 8_19.raw",
            path_prefix + "29_instrument blank_29.raw",
        ],
        "File name": [
            "1_instrumental blank_01",
            "4_Alkane mix_04",
            "6_instrumental blank_06",
            "7_procedural blank_07",
            "8_QC non-dilute_08",
            "11_QC 16_11",
            "12_QC 8_12",
            "15_QC non-dilute_15",
            "18_QC 4 _18",
            "19_QC 8_19",
            "29_instrument blank_29",
        ],
        "Type": [
            "Standard",
            "Standard",
            "Standard",
            "Blank",
            "QC",
            "QC",
            "QC",
            "QC",
            "QC",
            "QC",
            "Standard",
        ],
        "Class ID": [3, 5, 3, 6, 2, 2, 2, 2, 2, 2, 3],
        "Batch": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        "Analytical order": [1, 4, 6, 7, 8, 11, 12, 15, 18, 19, 29],
        "Inject. volume (μL)": [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
        "Included": [True, True, True, True, True, True, True, True, True, True, True],
    }

    return pd.DataFrame(data=d)


@pytest.fixture
def processed_dataframe() -> pd.DataFrame:
    """Creates a dataframe corresponding to processed metadata file.

    Returns:
        pd.DataFrame: Expected processed metadata dataframe.
    """
    d = {
        "sampleName": [
            "1_instrumental_blank_01",
            "4_Alkane_mix_04",
            "6_instrumental_blank_06",
            "7_procedural_blank_07",
            "8_QC_non-dilute_08",
            "11_QC_16_11",
            "12_QC_8_12",
            "15_QC_non-dilute_15",
            "18_QC_4_18",
            "19_QC_8_19",
            "29_instrument_blank_29",
        ],
        "sampleType": [
            "Standard",
            "Standard",
            "Standard",
            "Blank",
            "QC",
            "QC",
            "QC",
            "QC",
            "QC",
            "QC",
            "Standard",
        ],
        "class": [3, 5, 3, 6, 2, 2, 2, 2, 2, 2, 3],
        "batch": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        "injectionOrder": [1, 4, 6, 7, 8, 11, 12, 15, 18, 19, 29],
    }

    return pd.DataFrame(data=d)



@pytest.fixture
def alkanes() -> pd.DataFrame:
    """Creates a dataframe corresponding to processed alkane file.

    Returns:
        pd.DataFrame: Expected dataframe matching alkanes test file.
    """
    d = {
        "carbon_number": [12, 13, 14, 15, 16, 17, 18, 19, 20],
        "rt": [2.8, 3.0, 3.3, 3.7, 4.2, 4.6, 5.0, 5.4, 5.7],
    }

    return pd.DataFrame(data=d)


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


@pytest.mark.skip(reason="Test fails due to a inconsistency in the input file (metadata)")
def test_process_metadata_file(processed_dataframe: pd.DataFrame, tmp_path: str):
    """Tests processing the metadata file.

    Args:
        processed_dataframe (pd.DataFrame): Metadata dataframe.
        tmp_path (str): Path where the processed dataframe will be exported.
    """
    file_path = os.path.join("tests", "test_data", "batch_specification1.csv")
    out_path = os.path.join(tmp_path, "processed_batch_specification1.tsv")

    process_metadata_file(file_path, out_path) 
    actual = pd.read_csv(out_path, sep="\t")

    assert actual.equals(processed_dataframe)


def test_process_alkane_ri_file(alkanes: pd.DataFrame, tmp_path: str):
    """Tests processing of the alkanes input file.

    Args:
        alkanes (pd.DataFrame): An expected alkane dataframe.
        tmp_path (str): A path where the processed alkane file is exported.
    """
    file_path = os.path.join("tests", "test_data", "Alkane_RI_ATHLETE_1.txt")
    out_path = os.path.join(tmp_path, "processed_Alkane_RI_ATHLETE_1.tsv")

    process_alkane_ri_file(file_path, out_path) 
    actual = pd.read_csv(out_path, sep ="\t")

    assert actual.equals(alkanes)


def test_process_metadata_file_raise_columns_missing(tmp_path: str):
    file_path = os.path.join("tests", "test_data", "invalid_metadata.txt")
    out = os.path.join(tmp_path, "res.tsv")

    with pytest.raises(Exception) as e:
        process_metadata_file(file_path, out)
    
    assert str(e.value) == '"[\'File name\', \'Class ID\', \'Analytical order\'] not in index"'


@pytest.mark.parametrize("file_name, expected", [
    ["18_QC 4 _18", True],
    ["1_QC_1", True],
    ["blub", False],
    ["sample_0.56", False],
    ["_170", False]
])
def test_validate_filename(file_name, expected):
    assert validate_filename(file_name) == expected
