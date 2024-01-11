import re
from pathlib import Path


class AOCError(Exception):
    """Base Error"""


class AOCKeyError(AOCError):
    """Error for bad key values"""


class AOCAttributeError(AOCError):
    """Error for bad attributes"""


class AOCValueError(AOCError):
    """Error for bad values input or output"""


def read_input(file: Path) -> list[str]:
    """Read input.txt and return a list of stripped strings"""
    with open(file, "r") as fh:
        return [line.strip() for line in fh.readlines()]


def parse_line(line: str, divider=":", idx=1) -> str:
    """Parse a line"""
    # TODO: change to re use if m.match ...
    divided = line.split(divider)
    if len(divided) == 1:
        return ""
    return divided[idx].strip()


def parse_str_arr(array: str, divider: str = r"\s+") -> list[int]:
    """Parse an array of ints in a string, separated by separator
    Parameters
    ----------
    array : str
        string array e.g. " 5   6   7  10"
    divider : str
        dividing char or RE, defaults to r'\s+'

    Returns
    -------
    list[int]
        list of ints in str, e.g. [5, 6, 7, 10]"""
    m = re.compile(divider)
    if len(splitted := m.split(array.strip())) == 1:
        return []
    return [int(ele) for ele in splitted]


def concat_str_int(array: str, divider: str = r"\s+") -> list[int]:
    """Parse an array of ints in a string, separated by separator
    Parameters
    ----------
    array : str
        string array e.g. " 5   6   7  10"
    divider : str
        dividing char or RE, defaults to r'\s+'

    Returns
    -------
    list[int]
        list length of 1 of int in str, e.g. [56710]"""
    m = re.compile(divider)
    if len(splitted := m.split(array.strip())) == 1:
        return []
    return [int("".join(splitted))]
