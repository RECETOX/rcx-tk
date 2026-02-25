import pytest
from rcx_tk.utils import validate_filename


@pytest.mark.parametrize(
    "file_name, expected",
    [["18_QC 4 _18", True], ["1_QC_1", True], ["blub", False], ["sample_0.56", False], ["_170", False]],
)
def test_validate_filename(file_name: str, expected: bool):
    """Test to validate filenames."""
    assert validate_filename(file_name) == expected
