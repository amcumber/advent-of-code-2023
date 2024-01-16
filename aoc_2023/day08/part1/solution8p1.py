"""Solution to day 8 part 1"""
import sys
from pathlib import Path

if __name__ == "__main__":
    sys.path.append(str(Path(__file__).parent.resolve() / "../../.."))

from aoc_2023.core import read_input
from aoc_2023.day08.day8 import parse_directions, parse_map

START_KEY = "AAA"
END_KEY = "ZZZ"


def follow_directions_p1(
    directions: tuple[int],
    map_: dict[str, tuple[str, str]],
    *,
    start_key: str = START_KEY,
    current_count: int = 0,
    end_key: str = END_KEY,
) -> tuple[int, str, bool]:
    key = start_key
    these_directions = iter(directions)

    for next_dir in these_directions:
        fork = map_[key]
        key = fork[next_dir]
        current_count += 1
        if key == end_key:
            return current_count, key, True
    return current_count, key, False


def main(input_data: list[str]) -> int:
    """main for day8 part 1 - haunted wasteland"""
    directions = parse_directions(input_data)
    map_ = parse_map(input_data)

    count, key, finished = follow_directions_p1(directions, map_)
    while not finished:
        count, key, finished = follow_directions_p1(
            directions,
            map_,
            start_key=key,
            current_count=count,
        )
    return count


if __name__ == "__main__":
    input_file = Path(__file__).parent.parent / "input.txt"
    input_data = read_input(input_file)
    result = main(input_data)

    output_file = Path(__file__).parent / "result.txt"
    with open(output_file, "w") as fh:
        fh.write(str(result))
    print(f"The number of steps required are: {result}")
