from dataclasses import dataclass
import sys
from pathlib import Path

if __name__ == "__main__":
    sys.path.append(str(Path(__file__).parent.resolve() / "../../.."))

from aoc_2023.core import get_input_output_files, read_input, write_result
from aoc_2023.day11.day11 import (
    find_targets,
    get_dists,
    calc_result,
    TARGET_ID,
    expand_data,
)


def main(input_data: list[str]) -> list[int]:
    data = expand_data(input_data, target_id=TARGET_ID)
    targets = find_targets(data)
    return get_dists(targets)


if __name__ == "__main__":
    input_file, output_file = get_input_output_files(__file__)

    input_data = read_input(input_file)
    result = main(input_data)
    val = calc_result(result)

    write_result(output_file, val)
    print(f"The sum of data is: {val}")
