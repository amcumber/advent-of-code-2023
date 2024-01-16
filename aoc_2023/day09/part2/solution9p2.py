"""Solution to day 9 part 1"""
import math
import sys
from dataclasses import dataclass, field
from pathlib import Path

if __name__ == "__main__":
    sys.path.append(str(Path(__file__).parent.resolve() / "../../.."))

from aoc_2023.core import get_input_output_files, read_input, write_result
from aoc_2023.day09.day9 import Sequence, calc_result, parse_sequences


def main(input_data: list[str]) -> list[int]:
    seqs = parse_sequences(input_data)
    results = []
    for seq in seqs:
        model = Sequence(seq)
        model.fit()
        results.append(model.predict_backward())
    return results


if __name__ == "__main__":
    input_file, output_file = get_input_output_files(__file__)

    input_data = read_input(input_file)
    result = main(input_data)
    val = calc_result(result)

    write_result(output_file, val)
    print(f"The sum of extrapolated data is: {val}")
