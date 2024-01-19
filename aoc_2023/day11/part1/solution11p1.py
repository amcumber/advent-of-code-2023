from dataclasses import dataclass
import sys
from pathlib import Path

if __name__ == "__main__":
    sys.path.append(str(Path(__file__).parent.resolve() / "../../.."))

from aoc_2023.core import get_input_output_files, read_input, write_result

TARGET = "#"
MT = "."


@dataclass
class Coord:
    y: int
    x: int

    def __sub__(self, other) -> int:
        Y = self.y - other.y
        X = self.x - other.x
        return Y, X

    def dist(self, other) -> int:
        """Get manhattan distance"""
        d_y, d_x = other - self
        return abs(d_x) + abs(d_y)

    def tup(self) -> tuple[int]:
        return self.y, self.x


def transpose(data: list[str]) -> list[str]:
    """Transpose data"""
    return ["".join(col) for col in zip(*data)]


def is_row_empty(row: str, key: str = TARGET) -> bool:
    return not row.count(key)


def expand_data(data: list[str], blank: str = MT, target: str = TARGET) -> list[str]:
    def expand_rows(data):
        new_data = []
        for row in data:
            if is_row_empty(row, target):
                new_data.append(blank * len(row))
            new_data.append(row)
        return new_data

    def expand_cols(data):
        new_data = []
        for col in transpose(data):
            if is_row_empty(col, target):
                new_data.append(blank * len(col))
            new_data.append(col)
        return [row for row in transpose(new_data)]

    new_data = expand_rows(data)
    return expand_cols(new_data)


def find_targets(data: list[str], target: str = TARGET) -> list[Coord]:
    targets = []
    for y, row in enumerate(data):
        targets.extend(get_targets_in_row(row, y, target))
    return targets


def get_dists(targets: list[Coord]) -> list[int]:
    dists = []
    while len(targets):
        target = targets.pop(0)
        for other in targets:
            dists.append(target.dist(other))
    return dists


def get_targets_in_row(row: str, y: int, target: str = TARGET) -> list[Coord]:
    cnt = row.count(target)
    targets = []
    ref_idx = 0
    while cnt:
        x = row.find(target, ref_idx)
        targets.append(Coord(y, x))

        ref_idx = x + 1
        cnt -= 1
    return targets


def main(input_data: list[str]) -> list[int]:
    data = expand_data(input_data)
    targets = find_targets(data)
    return get_dists(targets)


def calc_result(val: list[int]) -> int:
    return sum(val)


if __name__ == "__main__":
    input_file, output_file = get_input_output_files(__file__)

    input_data = read_input(input_file)
    result = main(input_data)
    val = calc_result(result)

    write_result(output_file, val)
    print(f"The sum of data is: {val}")
