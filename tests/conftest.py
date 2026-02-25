from typing import Final
import pandas as pd
import pytest


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
