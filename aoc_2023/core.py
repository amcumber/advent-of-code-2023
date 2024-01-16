import re
from pathlib import Path
from typing import Any

ROOT = (Path(__file__).parent / "..").resolve()
OLD_BASE = ROOT / "aoc_2023"
USR_ROOT = ROOT / "usr"


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


def minus_root(root: Path, path: Path) -> Path:
    """Remove a root path from a path to make a relative path"""
    if not all([part in path.parts for part in root.parts]):
        raise AOCValueError("Not part of path")

    rel_path = list(path.parts)
    for part in root.parts:
        if 0 != rel_path.index(part):
            raise AOCValueError("Incorrect index, aborting")
        rel_path.pop(0)
    new_path = Path()
    for part in rel_path:
        new_path /= part
    return new_path


def get_new_root(path: Path, old_root: Path, new_root: Path) -> Path:
    """Replace one root path with a new root path for a given path"""
    old_root = old_root.resolve()
    new_root = new_root.resolve()
    path = path.resolve()
    rel_file = minus_root(old_root, path)
    return new_root / rel_file


def replace_file(file: Path, old_root: Path, new_root: Path) -> Path:
    new_file = get_new_root(file, old_root, new_root)
    new_file.parent.mkdir(exist_ok=True, parents=True)
    file.rename(new_file)


def write_result(file: Path, payload: Any):
    """write result to file, payload must have a __str__ method"""
    file.parent.mkdir(parents=True, exist_ok=True)
    with open(file, "w") as fh:
        fh.write(str(payload))


def get_input_output_files(puzzle_file: Path | str) -> tuple[Path, Path]:
    """Return location of input file and result file to be used in puzzle"""
    old_input = Path(puzzle_file).parent.parent / "input.txt"
    old_result = Path(puzzle_file).parent / "result.txt"

    return (
        get_new_root(x, OLD_BASE, USR_ROOT) for x in (old_input, old_result)
    )
