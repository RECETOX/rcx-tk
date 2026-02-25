import os
from pathlib import Path
from typing import Final
import pandas as pd
import pytest
from rcx_tk.sequence import add_local_order
from rcx_tk.sequence import add_sequence_identifier
from rcx_tk.sequence import add_subject_identifier
from rcx_tk.sequence import process_sequence_file
from rcx_tk.sequence import replace_spaces
from rcx_tk.sequence import separate_filename
from rcx_tk.sequence import validate_injection_order

__location__: Final[Path] = Path(__file__).parent.resolve()


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
            "18_QC_4__18",
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
        "sequenceIdentifier": [
            "1_instrumental blank",
            "4_Alkane mix",
            "6_instrumental blank",
            "7_procedural blank",
            "8_QC non-dilute",
            "11_QC 16",
            "12_QC 8",
            "15_QC non-dilute",
            "18_QC 4",
            "19_QC 8",
            "29_instrument blank",
        ],
        "subjectIdentifier": [
            "instrumental blank",
            "Alkane mix",
            "instrumental blank",
            "procedural blank",
            "QC non-dilute",
            "QC 16",
            "QC 8",
            "QC non-dilute",
            "QC 4",
            "QC 8",
            "instrument blank",
        ],
        "localOrder": [1, 4, 6, 7, 8, 11, 12, 15, 18, 19, 29],
    }

    return pd.DataFrame(data=d)


def test_process_metadata_file(processed_dataframe: pd.DataFrame, tmp_path: str):
    """Tests processing the metadata file.

    Args:
        processed_dataframe (pd.DataFrame): Metadata dataframe.
        tmp_path (str): Path where the processed dataframe will be exported.
    """
    file_path = os.path.join("tests", "test_data", "batch_specification1.csv")
    out_path = os.path.join(tmp_path, "processed_batch_specification1.tsv")

    process_sequence_file(file_path, out_path)
    actual = pd.read_csv(out_path, sep="\t")

    assert actual.equals(processed_dataframe)


def test_process_metadata_file_raise_columns_missing(tmp_path: str):
    """Test for raising exception if column is missing."""
    file_path = os.path.join("tests", "test_data", "invalid_metadata.txt")
    out = os.path.join(tmp_path, "res.tsv")

    with pytest.raises(Exception) as e:
        process_sequence_file(file_path, out)

    assert str(e.value) == "\"['File name', 'Class ID', 'Analytical order'] not in index\""


@pytest.mark.parametrize("file_name, expected", [["18_QC 4 _18", 18], ["1_QC_1", 1]])
def test_add_localOrder(file_name: str, expected: int):
    """Tests the add_localOrder function.

    Args:
        file_name (str): The filename.
        expected (int): The localOrder value.
    """
    actual = add_local_order(file_name)
    assert actual == expected


@pytest.mark.parametrize("file_name, expected", [["18_QC 4 _18", "18_QC 4"], ["1_QC_1", "1_QC"]])
def test_add_sequenceIdentifier(file_name: str, expected: str):
    """Tests the add_sequenceIdentifier function.

    Args:
        file_name (str): The filename.
        expected (str): The sequenceIdentifier value.
    """
    actual = add_sequence_identifier(file_name)
    assert actual == expected


@pytest.mark.parametrize("file_name, expected", [["18_QC 4 _18", "QC 4"], ["1_QC_1", "QC"], ["11_QC 16_11", "QC 16"]])
def test_add_subjectIdentifier(file_name: str, expected: str):
    """Tests the add_subjectIdentifier function.

    Args:
        file_name (str): The filename.
        expected (str): The subjectIdentifier value.
    """
    actual = add_subject_identifier(file_name)
    assert actual == expected


@pytest.mark.parametrize("file_name, expected", [["18_QC 4 _18", "18_QC_4__18"], ["1_QC_1", "1_QC_1"]])
def test_replace_fileName(file_name: str, expected: str):
    """Tests tge replace_fileName function.

    Args:
        file_name (str): The filename.
        expected (str): The filename with replaced spaces by underscores.
    """
    actual = replace_spaces(file_name)
    assert actual == expected


@pytest.mark.parametrize("file_name, expected", [["18_QC 4 _18", ("18_QC 4 _", "18")], ["1_QC_1", ("1_QC_", "1")]])
def test_separate_filename(file_name: str, expected: str):
    """Tests the regex to separate filenames.

    Args:
        file_name (str): The filename.
        expected (str): The splitted filename.
    """
    actual = separate_filename(file_name)
    assert actual == expected


@pytest.mark.parametrize(
    "dataFrame, expected",
    [[pd.DataFrame({"injectionOrder": [1, 4, 5]}), True], [pd.DataFrame({"injectionOrder": ["1", None, 5]}), False]],
)
def test_validateInjectionOrder(dataFrame: pd.DataFrame, expected: bool):
    """Tests the injection order validation function.

    Args:
        dataFrame (pd.DataFrame): A dataframe with injection order.
        expected (bool): Whether it is of integer (True) or other data type (False)
    """
    actual = validate_injection_order(dataFrame)
    assert expected == actual
