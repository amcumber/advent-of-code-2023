import math
import sys
from functools import reduce
from pathlib import Path

if __name__ == "__main__":
    sys.path.append(str(Path(__file__).parent.resolve() / "../../.."))

from aoc_2023.core import read_input
from aoc_2023.day06.day6 import get_races


def get_n_taus_above_record(record_tau: tuple[float, float], opt_tau: float) -> int:
    low, high = record_tau
    # correction for equal values
    low += 1e-6
    high -= 1e-6
    return len(range(math.ceil(low), math.ceil(high)))


def main(input_data: list[str]):
    races = get_races(input_data)
    n_solutions = []
    for race in races:
        record_taus = race.get_record_taus()
        opt_tau = race.get_optimal_tau()
        n_solutions.append(get_n_taus_above_record(record_taus, opt_tau))
    return n_solutions


def calc_result(result: list[int]):
    return reduce(lambda x, y: x * y, result)


if __name__ == "__main__":
    input_file = Path(__file__).parent.parent / "input.txt"
    input_data = read_input(input_file)
    result = main(input_data)
    val = calc_result(result)

    output_file = Path(__file__).parent / "result.txt"
    with open(output_file, "w") as fh:
        fh.write(str(val))
    print(f"The results are: {result} with a n_possible solution of: {val}")
