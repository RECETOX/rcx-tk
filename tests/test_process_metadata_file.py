from pathlib import Path
from typing import Final
import pandas as pd
import os
import pytest
from rcx_tk.process_metadata_file import read_file

__location__: Final[Path] = Path(__file__).parent.resolve()

@pytest.fixture 
def dataframe():
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
      "Inject. volume (uL)": [
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

@pytest.mark.parametrize("file_name",
                         ["batch_specification1.csv", "batch_specification1.xlsx", "batch_specification1.txt"])
def test_read_file(file_name, dataframe):
    file_path = __location__.joinpath("test_data", file_name)
    actual = read_file(str(file_path))
    assert actual.equals(dataframe)
    
