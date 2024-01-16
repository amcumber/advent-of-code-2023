"""Solution to day 9 part 1"""
import math
import sys
from dataclasses import dataclass, field
from pathlib import Path

if __name__ == "__main__":
    sys.path.append(str(Path(__file__).parent.resolve() / "../../.."))

from aoc_2023.core import parse_str_arr


def diff(x: list[int]):
    """get the difference between adjacent elements - forward looking"""
    return [idx - jdx for idx, jdx in zip(x[1:], x[:-1])]


@dataclass
class Sequence:
    x: list[int]
    tree: list[list[int]] = field(init=False, repr=False, default_factory=list)

    def fit(self) -> list[list[int]]:
        x_next = diff(self.x)
        while True:
            self.tree.append(x_next)
            if sum(x_next) == 0:
                return self.tree
            x = x_next
            x_next = diff(x)

    def predict(self) -> int:
        prev_pred = 0
        for leaf in reversed(self.tree):
            pred = leaf[-1] + prev_pred
            prev_pred = pred
        return pred + self.x[-1]

    def predict_backward(self) -> int:
        prev_pred = 0
        for leaf in reversed(self.tree):
            pred = leaf[0] - prev_pred
            prev_pred = pred
        return self.x[0] - pred


def parse_sequences(input_data: list[str]) -> list[list[int]]:
    seqs = []
    for line in input_data:
        seqs.append(parse_str_arr(line))
    return seqs


def calc_result(seq: list[int]) -> int:
    return sum(seq)
