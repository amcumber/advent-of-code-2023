import sys
from pathlib import Path

import pytest

if __name__ == "__main__":
    sys.path.append(str(Path(__file__).parent.resolve() / "../../.."))

from aoc_2023.day09.day9 import Sequence, calc_result
from aoc_2023.day09.part1.test_solution9p1 import (
    example_input,
    example_sequences,
)
from aoc_2023.day09.part2.solution9p2 import main


def example_prediction():
    return [-3, 0, 5]


def expected_result():
    return 2


@pytest.mark.parametrize(
    ["seq", "expected"],
    [
        (example_sequences()[0], example_prediction()[0]),
        (example_sequences()[1], example_prediction()[1]),
        (example_sequences()[2], example_prediction()[2]),
    ],
)
def test_sequence_pred_backward(seq, expected):
    model = Sequence(seq)
    model.fit()
    result = model.predict_backward()
    assert result == expected


@pytest.mark.parametrize(
    ["input_data", "expected"],
    [
        (example_input(), example_prediction()),
    ],
)
def test_main(input_data, expected):
    result = main(input_data)
    assert result == expected


@pytest.mark.parametrize(
    ["input_data", "expected"],
    [
        (example_input(), expected_result()),
    ],
)
def test_calc_result(input_data, expected):
    preds = main(input_data)
    result = calc_result(preds)

    assert result == expected
