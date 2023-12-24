from pathlib import Path
import re


def read_input(file: Path) -> list[str]:
    """Read input.txt and return a list of stripped strings"""
    with open(file, "r") as fh:
        return [line.strip() for line in fh.readlines()]


def parse_line(line: str, divider=":", idx=1) -> list[list[int]]:
    """Parse a line"""
    # TODO: change to re use if m.match ...
    divided = line.split(divider)[idx]
    return divided


def parse_str_arr(array: str, divider: str = r"\s+") -> list[int]:
    """Parse an array of ints in a string, separated by separator
    Parameters
    ----------
    array : str
        string array e.g. " 5   6   7  10"
    divider : str
        dividing char or RE

    Returns
    -------
    list[int]
        list of ints in str"""
    m = re.compile(divider)
    return [int(ele) for ele in m.split(array.strip())]
