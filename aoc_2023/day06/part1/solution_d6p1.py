import sys
from functools import reduce
from pathlib import Path

if __name__ == "__main__":
    sys.path.append(str(Path(__file__).parent.resolve() / "../../.."))

from aoc_2023.core import read_input
from aoc_2023.day06.day6 import get_optimal_tau, get_races, get_record_tau


def get_n_taus_above_record(opt_tau: float, record_tau: int) -> int:
    above_record = range(p1 := record_tau + 1, p1 + (c_t := round(opt_tau)))
    if c_t == (opt_tau * 2 // 2):
        return len(above_record)
    return len(above_record) + 1


def main(input_data: list[str]):
    races = get_races(input_data)
    n_solutions = []
    for race in races:
        record_tau = get_record_tau(race)
        opt_tau = get_optimal_tau(race)
        n_solutions.append(get_n_taus_above_record(opt_tau, record_tau))
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
