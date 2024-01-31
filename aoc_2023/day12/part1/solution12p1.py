from dataclasses import dataclass
import sys
from pathlib import Path

if __name__ == "__main__":
    sys.path.append(str(Path(__file__).parent.resolve() / "../../.."))

from aoc_2023.core import get_input_output_files, read_input, write_result


def main(input_data: list[str]) -> list[int]:
    return None


def calc_result(val: list[int]) -> int:
    return sum(val)


if __name__ == "__main__":
    input_file, output_file = get_input_output_files(__file__)

    input_data = read_input(input_file)
    result = main(input_data)
    val = calc_result(result)

    write_result(output_file, val)
    print(f"The sum of data is: {val}")
