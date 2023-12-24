import re
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.resolve() / "../../.."))

from aoc_2023.core import read_input


def _parse_line(line: str) -> list[list[int]]:
    winner_str, card_str = line.split(":")[1].split("|")
    return tuple(_parse_str_arr(arr) for arr in (winner_str, card_str))


def _parse_str_arr(array: str) -> list[int]:
    m = re.compile(r"\s+")
    return [int(ele) for ele in m.split(array.strip())]


def parse_input(lines: list[str]) -> tuple[list[int], list[int]]:
    return zip(*[_parse_line(line) for line in lines])


def get_matches(card, winners) -> list[int]:
    return [num for num in card if num in winners]
