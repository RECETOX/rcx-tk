from typing import Any


def validate_filename(file_name: str) -> bool:
    """Validate a filename.

    Args:
        file_name (str): Filename to validate.

    Returns:
        bool: Validity of the filename.
    """

    def is_not_empty(x: str) -> bool:
        return x != ""

    tokens: list[str] = list(filter(is_not_empty, file_name.split("_")))
    return len(tokens) > 1 and tokens[-1].isdigit()


def replace_spaces(file_name: str) -> str:
    """Replaces spaces with underscores in Filename.

    Args:
        file_name (str): The filename.

    Returns:
        str: The replaced filename.
    """
    x = file_name.replace(" ", "_")
    return x


def concat_str(value: Any) -> str:
    """Join values that can be cast to string together into single string, elements separated by ,.

    Args:
        value (Any): Set of items to concatenate

    Returns:
        str: Joined result string.
    """
    return ",".join(map(str, value))
