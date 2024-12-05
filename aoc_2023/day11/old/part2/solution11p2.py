import sys
from pathlib import Path

if __name__ == "__main__":
    sys.path.append(str(Path(__file__).parent.resolve() / "../../.."))

from aoc_2023.core import get_input_output_files, read_input, write_result
from aoc_2023.day11.old.day11 import (
    calc_result,
    expand_data,
    find_targets,
    get_dists,
)

INFILL = "@"
INFILL_VAL = 1_000_000


def main(input_data: list[str], infill_id: str, infill_val: int) -> list[int]:
    data = expand_data(
        input_data,
        infill_id=infill_id,
    )
    targets = find_targets(
        data,
        infill_id=infill_id,
        infill_val=infill_val,
    )
    return get_dists(targets)


if __name__ == "__main__":
    input_file, output_file = get_input_output_files(__file__)

    input_data = read_input(input_file)
    result = main(input_data, INFILL, INFILL_VAL)
    val = calc_result(result)

    write_result(output_file, val)
    print(f"The sum of data is: {val}")
