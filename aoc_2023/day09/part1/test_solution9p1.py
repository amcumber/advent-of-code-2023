import sys
from pathlib import Path

import pytest

if __name__ == "__main__":
    sys.path.append(str(Path(__file__).parent.resolve() / "../../.."))

from aoc_2023.day09.day9 import Sequence, calc_result, diff, parse_sequences
from aoc_2023.day09.part1.solution9p1 import main


def example_input():
    return [
        "0 3 6 9 12 15",
        "1 3 6 10 15 21",
        "10 13 16 21 30 45",
    ]


def example_sequences():
    return [
        [0, 3, 6, 9, 12, 15],
        [1, 3, 6, 10, 15, 21],
        [10, 13, 16, 21, 30, 45],
    ]


def example_sequence_tree1():
    return [
        [3, 3, 3, 3, 3],
        [0, 0, 0, 0],
    ]


def example_sequence_tree2():
    return [
        [2, 3, 4, 5, 6],
        [1, 1, 1, 1],
        [0, 0, 0],
    ]


def example_sequence_tree3():
    return [
        [3, 3, 5, 9, 15],
        [0, 2, 4, 6],
        [2, 2, 2],
        [0, 0],
    ]


def example_prediction():
    return [18, 28, 68]


def expected_result():
    return 114


@pytest.mark.parametrize(
    ["input_data", "expected"],
    [(example_input(), example_sequences())],
)
def test_parse_sequences(input_data, expected):
    results = parse_sequences(input_data)
    assert results == expected


@pytest.mark.parametrize(
    ["seq", "expected"],
    [
        (example_sequences()[0], example_sequence_tree1()[0]),
        (example_sequences()[1], example_sequence_tree2()[0]),
        (example_sequences()[2], example_sequence_tree3()[0]),
    ],
)
def test_diff(seq, expected):
    result = diff(seq)
    assert result == expected


@pytest.mark.parametrize(
    ["seq", "expected"],
    [
        (example_sequences()[0], example_sequence_tree1()),
        (example_sequences()[1], example_sequence_tree2()),
        (example_sequences()[2], example_sequence_tree3()),
    ],
)
def test_sequence_fit(seq, expected):
    model = Sequence(seq)
    result = model.fit()
    assert result == expected


@pytest.mark.parametrize(
    ["seq", "expected"],
    [
        (example_sequences()[0], example_prediction()[0]),
        (example_sequences()[1], example_prediction()[1]),
        (example_sequences()[2], example_prediction()[2]),
    ],
)
def test_sequence_pred(seq, expected):
    model = Sequence(seq)
    model.fit()
    result = model.predict()
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
