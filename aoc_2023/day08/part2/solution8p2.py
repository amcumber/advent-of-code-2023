"""solution to day 8 part 2"""

import sys
from math import lcm
from pathlib import Path

if __name__ == "__main__":
    sys.path.append(str(Path(__file__).parent.resolve() / "../../.."))

from aoc_2023.core import read_input
from aoc_2023.day08.day8 import parse_directions, parse_map

START_KEY_ID = "A"
END_KEY_ID = "Z"


def get_start_keys(
    map_: dict[str, int], start_key_id: str = START_KEY_ID
) -> list[str]:
    return [key for key in map_.keys() if start_key_id in key]


def follow_directions_p2(
    directions: tuple[int],
    map_: dict[str, tuple[str, str]],
    start_key: str,
    *,
    current_count: int = 0,
    end_key: str = END_KEY_ID,
) -> tuple[int, str, bool]:
    key = start_key
    these_directions = iter(directions)

    for next_dir in these_directions:
        fork = map_[key]
        key = fork[next_dir]
        current_count += 1
        if end_key in key:
            return current_count, key, True
    return current_count, key, False


def walk_key(
    directions: tuple[int],
    map_: dict[str, tuple[str, str]],
    start_key: str,
) -> int:
    count, key, finished = follow_directions_p2(directions, map_, start_key)
    while not finished:
        count, key, finished = follow_directions_p2(
            directions,
            map_,
            start_key=key,
            current_count=count,
        )
    return count


def main(input_data: list[str]) -> int:
    """main for day8 part 1 - haunted wasteland"""
    directions = parse_directions(input_data)
    map_ = parse_map(input_data)
    start_keys = get_start_keys(map_)
    return [walk_key(directions, map_, key) for key in start_keys]


def calc_result(min_counts: list[int]) -> int:
    return lcm(*min_counts)


if __name__ == "__main__":
    input_file = Path(__file__).parent.parent / "input.txt"
    input_data = read_input(input_file)
    result = main(input_data)
    val = calc_result(result)

    output_file = Path(__file__).parent / "result.txt"
    with open(output_file, "w") as fh:
        fh.write(str(val))
    print(f"The number of steps required are: {val}, from steps {result!r}")
