import pytest

import sys
from pathlib import Path

if __name__ == "__main__":
    sys.path.append(str(Path(__file__).parent.resolve() / "../../.."))

from aoc_2023.day11.part2.solution11p2 import main, INFILL
from aoc_2023.day11.day11 import (
    calc_result,
    expand_data,
    get_dists,
    find_targets,
)


def example_input():
    return [
        "...#......",
        ".......#..",
        "#.........",
        "..........",
        "......#...",
        ".#........",
        ".........#",
        "..........",
        ".......#..",
        "#...#.....",
    ]


def expanded_data():
    return [
        "..@#.@..@.",
        "..@..@.#@.",
        "#.@..@..@.",
        "@@@@@@@@@@",
        "..@..@#.@.",
        ".#@..@..@.",
        "..@..@..@#",
        "@@@@@@@@@@",
        "..@..@.#@.",
        "#.@.#@..@.",
    ]


def exp_coords(x: int = 2):
    return [
        (0, 2 + x),
        (1, 5 + 2 * x),
        (2, 0),
        (3 + x, 4 + 2 * x),
        (4 + x, 1),
        (5 + x, 6 + 3 * x),
        (6 + 2 * x, 4 + 2 * x),
        (7 + 2 * x, 0),
        (7 + 2 * x, 3 + x),
    ]


def expected_result10():
    return 1030


def expected_result100():
    return 8410


def data17(x):
    data = [
        "..@#.@..@.",
        "..@..@..@.",
        "..@..@..@.",
        "@@@@@@@@@@",
        "..@..@..@.",
        "..@..@..@.",
        "..@..@..@.",
        "@@@@@@@@@@",
        "..@..@.#@.",
        "..@..@..@.",
    ]
    result = [6 + 2 * x + 3 + x]
    return data, result


def data36(x):
    data = [
        "..@..@..@.",
        "..@..@..@.",
        "#.@..@..@.",
        "@@@@@@@@@@",
        "..@..@..@.",
        "..@..@..@.",
        "..@..@..@#",
        "@@@@@@@@@@",
        "..@..@..@.",
        "..@..@..@.",
    ]
    result = [6 + 3 * x + 3 + x]
    return data, result


def data89(x):
    data = [
        "#.@.#.......",
    ]
    result = [3 + x]
    return data, result


@pytest.mark.parametrize(
    ["input_data", "infill_val", "expected"],
    [
        (example_input(), 10, expected_result10()),
        (example_input(), 100, expected_result100()),
    ],
)
def test_calc_results(input_data, infill_val, expected):
    value = main(input_data, infill_val)
    results = calc_result(value)

    assert results == expected


@pytest.mark.parametrize(
    ["infill_val", "data", "expected"],
    [
        (2, *data17(2)),
        (2, *data36(2)),
        (2, *data89(2)),
        (10, *data17(10)),
        (10, *data36(10)),
        (10, *data89(10)),
        (100, *data17(100)),
        (100, *data36(100)),
        (100, *data89(100)),
    ],
)
def test_get_dists(infill_val, data, expected):
    targets = find_targets(data, infill_val=infill_val, infill_id=INFILL)
    results = get_dists(targets)
    assert results == expected


@pytest.mark.parametrize(
    ["data", "expected"],
    [
        (example_input(), expanded_data()),
    ],
)
def test_expand_data(data, expected):
    result = expand_data(data, infill_id=INFILL)
    for r, e in zip(result, expected):
        assert r == e


def test_find_targets(data, infill_val, expected):
    data_fixed = expand_data(data, infill_id=INFILL)
    find_targets(
        data_fixed,
        infill_id=INFILL,
        infill_val=infill_val,
    )
