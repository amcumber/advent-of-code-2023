"""Solution to day x part y"""
import sys
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Protocol

if __name__ == "__main__":
    sys.path.append(str(Path(__file__).parent.resolve() / "../../.."))

from aoc_2023.core import (
    AOCValueError,
    get_input_output_files,
    read_input,
    write_result,
)

START_POINT = "S"


class IndexPointType(Protocol):
    x: int
    y: int


@dataclass
class IndexPoint:
    y: int
    x: int
    max_y: int = field(repr=False, default=256)
    max_x: int = field(repr=False, default=256)
    idx: int = field(repr=False, init=False, default=0)

    def __iter__(self):
        return iter(self.this)

    @property
    def max_(self):
        return self.max_y, self.max_x

    @property
    def right(self):
        if self.x == self.max_x:
            return None
        return self.__class__(self.y, self.x + 1, *self.max_)

    @property
    def left(self):
        if self.x == 0:
            return None
        return self.__class__(self.y, self.x - 1, *self.max_)

    @property
    def up(self):
        if self.y == 0:
            return None
        return self.__class__(self.y - 1, self.x, *self.max_)

    @property
    def down(self):
        if self.y == self.max_y:
            return None
        return self.__class__(self.y + 1, self.x, *self.max_)

    @property
    def this(self):
        return self.y, self.x

    def __getitem__(self, value):
        return self.this[value]

    def __eq__(self, __value: object) -> bool:
        self.this == __value.this

    def __ne__(self, __value: object) -> bool:
        self.this != __value.this


@dataclass
class PipeMaze:
    map_: list[str]
    U2L: str = field(repr=False, default="J")
    U2R: str = field(repr=False, default="L")
    D2L: str = field(repr=False, default="7")
    D2R: str = field(repr=False, default="F")
    U2D: str = field(repr=False, default="|")
    L2R: str = field(repr=False, default="-")

    def __post_init__(self):
        self.left_connected = (self.U2L, self.D2L, self.L2R)
        self.right_connected = (self.U2R, self.D2R, self.L2R)
        self.up_connected = (self.U2R, self.U2L, self.U2D)
        self.down_connected = (self.D2R, self.D2L, self.U2D)

    def get_left_val(self, point: IndexPoint) -> str:
        return self[point.left]

    def get_right_val(self, point: IndexPoint) -> str:
        return self[point.right]

    def get_up_val(self, point: IndexPoint) -> str:
        return self[point.up]

    def get_down_val(self, point: IndexPoint) -> str:
        return self[point.down]

    def __getitem__(self, value: IndexPoint):
        if value is None:
            return None
        return self.map_[value.y][value.x]

    def is_left_connected(self, point: IndexPoint) -> bool:
        return self.get_left_val(point) in self.left_connected

    def is_right_connected(self, point: IndexPoint) -> bool:
        return self.get_right_val(point) in self.right_connected

    def is_up_connected(self, point: IndexPoint) -> bool:
        return self.get_up_val(point) in self.up_connected

    def is_down_connected(self, point: IndexPoint) -> bool:
        return self.get_down_val(point) in self.down_connected


def find_start(
    input_data: list[str], start_point: str = START_POINT
) -> IndexPoint:
    max_vals = get_max_vals(input_data)
    for idy, line in enumerate(input_data):
        if start_point in line:
            idx = line.find(start_point)
            return IndexPoint(idy, idx, *max_vals)
    raise AOCValueError(f"Bad input, cannot find start_point: {start_point}")


def get_max_vals(input_data: list[str]):
    max_y = len(input_data) - 1
    max_x = len(input_data[0]) - 1
    return max_y, max_x


def find_connections(
    maze: PipeMaze, point: IndexPoint, prev_points: IndexPoint
):
    connections = [
        (point.down, maze.is_down_connected(point)),
        (point.up, maze.is_up_connected(point)),
        (point.left, maze.is_left_connected(point)),
        (point.right, maze.is_right_connected(point)),
    ]
    new_points = [
        new_pnt for new_pnt, is_connected in connections if is_connected
    ]
    for prev_point in prev_points:
        if prev_point in new_points:
            new_points.pop(new_points.index(prev_point))
    return new_points


def find_path(maze: PipeMaze, start_point: IndexPoint) -> int:
    step = 0
    points = [start_point]
    prev_points = []
    while True:
        new_points = []
        step += 1
        for point in points:
            next_points = find_connections(maze, point, prev_points)
            # FIXME: bug here - not finding next connection
            if any([point in new_points for point in next_points]):
                break
            new_points.extend(next_points)
        prev_points = points
        points = new_points
    return step


def main(input_data: list[str]) -> list[int]:
    start_point = find_start(input_data)
    maze = PipeMaze(input_data)
    return find_path(maze, start_point)


def calc_result(seq: list[int]) -> int:
    return sum(seq)


if __name__ == "__main__":
    input_file, output_file = get_input_output_files(__file__)

    input_data = read_input(input_file)
    result = main(input_data)
    val = calc_result(result)

    write_result(output_file, val)
    print(f"The solution: {val}")
