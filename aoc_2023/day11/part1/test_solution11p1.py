import pytest

import sys
from pathlib import Path

if __name__ == "__main__":
    sys.path.append(str(Path(__file__).parent.resolve() / "../../.."))

from aoc_2023.day11.part1.solution11p1 import (
    main,
    calc_result,
    get_dists,
    transpose,
    expand_data,
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
        "....#........",
        ".........#...",
        "#............",
        ".............",
        ".............",
        "........#....",
        ".#...........",
        "............#",
        ".............",
        ".............",
        ".........#...",
        "#....#.......",
    ]


def exp_coords():
    return [
        (0, 4),
        (1, 9),
        (2, 0),
        (5, 8),
        (6, 1),
        (7, 12),
        (10, 9),
        (11, 0),
        (11, 5),
    ]


def exp_transpose():
    data = ["#.", "#."]
    result = ["##", ".."]
    return data, result


def expected_result():
    return 374


def data17():
    data = [
        "....#........",
        ".............",
        ".............",
        ".............",
        ".............",
        ".............",
        ".............",
        ".............",
        ".............",
        ".............",
        ".........#...",
        ".............",
    ]
    result = [15]
    return data, result


def data36():
    data = [
        ".............",
        ".............",
        "#............",
        ".............",
        ".............",
        ".............",
        ".............",
        "............#",
        ".............",
        ".............",
        ".............",
        ".............",
    ]
    result = [17]
    return data, result


def data89():
    data = [
        "#....#.......",
    ]
    result = [5]
    return data, result


def data59():
    data = [
        ".............",
        ".............",
        ".............",
        ".............",
        ".............",
        ".............",
        ".#...........",
        ".............",
        ".............",
        ".............",
        ".............",
        ".....#.......",
    ]
    result = [9]
    return data, result


@pytest.mark.parametrize(
    ["input_data", "expected"],
    [
        (example_input(), expected_result()),
    ],
)
def test_calc_results(input_data, expected):
    value = main(input_data)
    results = calc_result(value)

    assert results == expected


@pytest.mark.parametrize(
    ["data", "expected"],
    [
        data17(),
        data36(),
        data59(),
        data89(),
    ],
)
def test_get_dists(data, expected):
    targets = find_targets(data)
    results = get_dists(targets)
    assert results == expected


@pytest.mark.parametrize(
    ["data", "expected"],
    [
        (example_input(), expanded_data()),
    ],
)
def test_expand_data(data, expected):
    result = expand_data(data)
    for r, e in zip(result, expected):
        assert r == e


@pytest.mark.parametrize(
    ["data", "expected"],
    [
        exp_transpose(),
    ],
)
def test_transpose(data, expected):
    result = transpose(data)
    for r, e in zip(result, expected):
        assert r == e


@pytest.mark.parametrize(
    ["data", "expected"],
    [
        (expanded_data(), exp_coords()),
    ],
)
def test_transpose(data, expected):
    result = find_targets(data)
    res_tup = [r.tup() for r in result]
    for r in res_tup:
        assert r in expected, "Failed r in e"
    for e in expected:
        assert e in res_tup, "Failed e in r"
