import os
import pandas as pd
import pytest
from rcx_tk.alkanes import process_alkane_file


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


def test_process_alkane_ri_file(alkanes: pd.DataFrame, tmp_path: str):
    """Tests processing of the alkanes input file.

    Args:
        alkanes (pd.DataFrame): An expected alkane dataframe.
        tmp_path (str): A path where the processed alkane file is exported.
    """
    file_path = os.path.join("tests", "test_data", "Alkane_RI_ATHLETE_1.txt")
    out_path = os.path.join(tmp_path, "processed_Alkane_RI_ATHLETE_1.tsv")

    process_alkane_file(file_path, out_path)
    actual = pd.read_csv(out_path, sep="\t")

    assert actual.equals(alkanes)
