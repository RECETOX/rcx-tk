from pathlib import Path
from typing import Final
import pandas as pd
import os
import pytest
from rcx_tk.process_metadata_file import read_file, save_dataframe_as_tsv, process_metadata_file, process_alkane_ri_file

__location__: Final[Path] = Path(__file__).parent.resolve()

@pytest.fixture 
def dataframe():
    d = {
        'File path': [
            "Z:\\000020-Shares\\hram\\MS_omics\\Personal Folders\\COUFALIKOVA Katerina\\ATHLETE\\finalni data zaloha\\batch1-20231121-Katerina Coufalikova\\RAW_profile\\1_instrumental blank_01.raw",
            "Z:\\000020-Shares\\hram\\MS_omics\\Personal Folders\\COUFALIKOVA Katerina\\ATHLETE\\finalni data zaloha\\batch1-20231121-Katerina Coufalikova\\RAW_profile\\4_Alkane mix_04.raw",
            "Z:\\000020-Shares\\hram\\MS_omics\\Personal Folders\\COUFALIKOVA Katerina\\ATHLETE\\finalni data zaloha\\batch1-20231121-Katerina Coufalikova\\RAW_profile\\18_QC 4 _18.raw"
        ],
        'File name': [
            "1_instrumental blank_01",
            "4_Alkane mix_04",
            "18_QC 4 _18"
        ],
        "Analytical order": [
            1,
            4,
            18
        ],
         "Inject. volume (μL)": [
            6,
            6,
            6
        ]
    }

    return pd.DataFrame(data = d)


@pytest.fixture 
def processed_dataframe():
    d = {
        'sampleName': [
            "1_instrumental_blank_01",
            "4_Alkane_mix_04",
            "18_QC_4_18"
        ],
         "injectionOrder": [
            1,
            4,
            18
        ]
    }

    return pd.DataFrame(data = d)

@pytest.fixture
def alkanes():
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
                         ["batch_specification_specChar.csv", "batch_specification_specChar.xlsx", "batch_specification_specChar.txt"])
def test_read_file(file_name, dataframe):
    file_path = __location__.joinpath("test_data", file_name)
    #file_path = os.path.join("tests", "test_data", file_name)
    actual = read_file(str(file_path))
    assert actual.equals(dataframe)

def test_read_file_error(dataframe):
    file_path = os.path.join("tests", "test_data", "batch_specification1.prn")
    with pytest.raises(ValueError, match = r"Unsupported file format. Please provide a CSV, Excel, or TSV file."):
        read_file(file_path)

def test_save_dataframe_as_tsv(dataframe, tmp_path):
    out_path = os.path.join(tmp_path, "batch_specification1.tsv")
    save_dataframe_as_tsv(dataframe, out_path)
    actual = pd.read_csv(out_path, sep='\t')
    assert actual.equals(dataframe)

def test_read_save_dataframe_as_tsv_error(dataframe, tmp_path):
    out_path = os.path.join(tmp_path, "batch_specification1.prn")
    with pytest.raises(ValueError, match = r"Unsupported file format. Please point to a TSV file."):
        save_dataframe_as_tsv(dataframe, out_path)

def test_process_metadata_file(processed_dataframe, tmp_path):
    file_path = os.path.join("tests", "test_data", "batch_specification1.csv")
    out_path = os.path.join(tmp_path, "processed_batch_specification1.tsv")
    process_metadata_file(file_path, out_path) 
    actual = pd.read_csv(out_path, sep='\t')
    assert actual.equals(processed_dataframe)

def test_process_alkane_ri_file(alkanes, tmp_path):
    file_path = os.path.join("tests", "test_data", "Alkane_RI_ATHLETE_1.txt")
    out_path = os.path.join(tmp_path, "processed_Alkane_RI_ATHLETE_1.tsv")
    process_alkane_ri_file(file_path, out_path) 
    actual = pd.read_csv(out_path, sep ='\t')
    assert actual.equals(alkanes)