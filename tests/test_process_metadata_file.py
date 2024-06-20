from pathlib import Path
from typing import Final
import pandas as pd
import os
import pytest
from rcx_tk.process_metadata_file import read_file, save_dataframe_as_tsv, process_metadata_file, process_alkane_ri_file, validate_filename

__location__: Final[Path] = Path(__file__).parent.resolve()


@pytest.fixture 
def dataframe() -> pd.DataFrame:
    d = {
        'File path': [
            "Z:\\000020-Shares\\hram\\MS_omics\\Personal Folders\\COUFALIKOVA Katerina\\ATHLETE\\finalni data zaloha\\batch1-20231121-Katerina Coufalikova\\RAW_profile\\1_instrumental blank_01.raw",
            "Z:\\000020-Shares\\hram\\MS_omics\\Personal Folders\\COUFALIKOVA Katerina\\ATHLETE\\finalni data zaloha\\batch1-20231121-Katerina Coufalikova\\RAW_profile\\4_Alkane mix_04.raw",
            "Z:\\000020-Shares\\hram\\MS_omics\\Personal Folders\\COUFALIKOVA Katerina\\ATHLETE\\finalni data zaloha\\batch1-20231121-Katerina Coufalikova\\RAW_profile\\6_instrumental blank_06.raw",
            "Z:\\000020-Shares\\hram\\MS_omics\\Personal Folders\\COUFALIKOVA Katerina\\ATHLETE\\finalni data zaloha\\batch1-20231121-Katerina Coufalikova\\RAW_profile\\7_procedural blank_07.raw",
            "Z:\\000020-Shares\\hram\\MS_omics\\Personal Folders\\COUFALIKOVA Katerina\\ATHLETE\\finalni data zaloha\\batch1-20231121-Katerina Coufalikova\\RAW_profile\\8_QC non-dilute_08.raw",
            "Z:\\000020-Shares\\hram\\MS_omics\\Personal Folders\\COUFALIKOVA Katerina\\ATHLETE\\finalni data zaloha\\batch1-20231121-Katerina Coufalikova\\RAW_profile\\11_QC 16_11.raw",
            "Z:\\000020-Shares\\hram\\MS_omics\\Personal Folders\\COUFALIKOVA Katerina\\ATHLETE\\finalni data zaloha\\batch1-20231121-Katerina Coufalikova\\RAW_profile\\12_QC 8_12.raw",
            "Z:\\000020-Shares\\hram\\MS_omics\\Personal Folders\\COUFALIKOVA Katerina\\ATHLETE\\finalni data zaloha\\batch1-20231121-Katerina Coufalikova\\RAW_profile\\15_QC non-dilute_15.raw",
            "Z:\\000020-Shares\\hram\\MS_omics\\Personal Folders\\COUFALIKOVA Katerina\\ATHLETE\\finalni data zaloha\\batch1-20231121-Katerina Coufalikova\\RAW_profile\\18_QC 4 _18.raw",
            "Z:\\000020-Shares\\hram\\MS_omics\\Personal Folders\\COUFALIKOVA Katerina\\ATHLETE\\finalni data zaloha\\batch1-20231121-Katerina Coufalikova\\RAW_profile\\19_QC 8_19.raw",
            "Z:\\000020-Shares\\hram\\MS_omics\\Personal Folders\\COUFALIKOVA Katerina\\ATHLETE\\finalni data zaloha\\batch1-20231121-Katerina Coufalikova\\RAW_profile\\29_instrument blank_29.raw"
        ],
        'File name': [
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
            "29_instrument blank_29"
        ],
       'Type': [
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
            "Standard"
       ],
       "Class ID": [
            3,
            5,
            3,
            6,
            2,
            2,
            2,
            2,
            2,
            2,
            3
       ],
       "Batch": [
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1
       ],
      "Analytical order": [
            1,
            4,
            6,
            7,
            8,
            11,
            12,
            15,
            18,
            19,
            29
      ],
      "Inject. volume (μL)": [
            6,
            6,
            6,
            6,
            6,
            6,
            6,
            6,
            6,
            6,
            6
      ],
       "Included": [
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True
       ]
    }

    return pd.DataFrame(data = d)

@pytest.fixture 
def processed_dataframe() -> pd.DataFrame:
    d = {
        'sampleName': [
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
            "29_instrument_blank_29"
        ],
       'sampleType': [
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
            "Standard"
       ],
       "class": [
            3,
            5,
            3,
            6,
            2,
            2,
            2,
            2,
            2,
            2,
            3
       ],
       "batch": [
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1
       ],
      "injectionOrder": [
            1,
            4,
            6,
            7,
            8,
            11,
            12,
            15,
            18,
            19,
            29
      ]
    }

    return pd.DataFrame(data = d)


@pytest.fixture
def alkanes() -> pd.DataFrame:
    d = {
        "carbon_number": [
            12, 13, 14, 15, 16, 17, 18, 19, 20
        ],
        "rt": [
            2.8, 3.0, 3.3, 3.7, 4.2, 4.6, 5.0, 5.4, 5.7
        ]
    }

    return pd.DataFrame(data = d)


@pytest.mark.parametrize("file_name",
                         ["batch_specification1.csv", "batch_specification1.xlsx", "batch_specification1.txt"])
def test_read_file(file_name: str, dataframe: pd.DataFrame):
    # arrange
    file_path = __location__.joinpath("test_data", file_name)
    # act
    actual = read_file(str(file_path))
    # assert
    assert actual.equals(dataframe)


def test_read_file_error():
    file_path = os.path.join("tests", "test_data", "batch_specification1.prn")
    with pytest.raises(ValueError, match = r"Unsupported file format. Please provide a CSV, Excel, or TSV file."):
        read_file(file_path)


def test_save_dataframe_as_tsv(dataframe: pd.DataFrame, tmp_path: str):
    out_path = os.path.join(tmp_path, "batch_specification1.tsv")

    save_dataframe_as_tsv(dataframe, out_path)
    actual = pd.read_csv(out_path, sep='\t')

    assert actual.equals(dataframe)


def test_read_save_dataframe_as_tsv_error(dataframe: pd.DataFrame, tmp_path: str):
    out_path = os.path.join(tmp_path, "batch_specification1.prn")
    with pytest.raises(ValueError, match = r"Unsupported file format. Please point to a TSV file."):
        save_dataframe_as_tsv(dataframe, out_path)


def test_process_metadata_file(processed_dataframe: pd.DataFrame, tmp_path: str):
    file_path = os.path.join("tests", "test_data", "batch_specification1.csv")
    out_path = os.path.join(tmp_path, "processed_batch_specification1.tsv")

    process_metadata_file(file_path, out_path) 
    actual = pd.read_csv(out_path, sep='\t')

    assert actual.equals(processed_dataframe)


def test_process_alkane_ri_file(alkanes: pd.DataFrame, tmp_path: str):
    file_path = os.path.join("tests", "test_data", "Alkane_RI_ATHLETE_1.txt")
    out_path = os.path.join(tmp_path, "processed_Alkane_RI_ATHLETE_1.tsv")

    process_alkane_ri_file(file_path, out_path) 
    actual = pd.read_csv(out_path, sep ='\t')

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