import pytest
from aoc_2023.day12.soln import calc_result, main_part1


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
    result = main_part1(input_data)

    assert result == expected

