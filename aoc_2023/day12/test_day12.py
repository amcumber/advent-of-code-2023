import sys
from pathlib import Path

import pytest
from aoc_2023.day12.soln import calc_result, main


def example_input1():
    return [
        "???.### 1,1,3",
        ".??..??...?##. 1,1,3",
        "?#?#?#?#?#?#?#? 1,3,1,6",
        "????.#...#... 4,1,1",
        "????.######..#####. 1,6,5",
        "?###???????? 3,2,1",
    ]


def example_input2():
    return [
        "#.#.### 1,1,3",
        ".#...#....###. 1,1,3",
        ".#.###.#.###### 1,3,1,6",
        "####.#...#... 4,1,1",
        "#....######..#####. 1,6,5",
        ".###.##....# 3,2,1",
    ]


def expected_arrangements1():
    return [1, 4, 1, 1, 4, 10]


def expected_arrangements2():
    return [1, 1, 1, 1, 1, 1]


def expected_result1():
    return 21


def expected_result2():
    return 6


@pytest.mark.parametrize(
    ["input_data", "expected"],
    [
        (example_input1(), expected_arrangements1()),
        (example_input2(), expected_arrangements2()),
    ],
)
def test_main(input_data, expected):
    result = main(input_data)

    assert result == expected


@pytest.mark.parametrize(
    ["input_data", "expected"],
    [
        (example_input1(), expected_result1()),
        (example_input2(), expected_result2()),
    ],
)
def test_calc_results(input_data, expected):
    value = main(input_data)
    results = calc_result(value)

    assert results == expected
