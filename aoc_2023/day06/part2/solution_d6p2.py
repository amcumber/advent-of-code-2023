import sys
from pathlib import Path

if __name__ == "__main__":
    sys.path.append(str(Path(__file__).parent.resolve() / "../../.."))

from aoc_2023.core import read_input
from aoc_2023.day06.day6 import (
    calc_result,
    get_n_taus_above_record,
    get_races,
    parse_dists_p2,
    parse_times_p2,
)


def main(input_data: list[str]):
    races = get_races(input_data, parse_times_p2, parse_dists_p2)
    n_solutions = []
    for race in races:
        record_taus = race.get_record_taus()
        opt_tau = race.get_optimal_tau()
        n_solutions.append(get_n_taus_above_record(record_taus, opt_tau))
    return n_solutions


if __name__ == "__main__":
    input_file = Path(__file__).parent.parent / "input.txt"
    input_data = read_input(input_file)
    result = main(input_data)
    val = calc_result(result)

    output_file = Path(__file__).parent / "result.txt"
    with open(output_file, "w") as fh:
        fh.write(str(val))
    print(f"The results are: {result} with a n_possible solution of: {val}")
