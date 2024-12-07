import pytest
from aoc_2023.day12 import soln


@pytest.fixture
def input_():
    return [
        "???.### 1,1,3",
        ".??..??...?##. 1,1,3",
        "?#?#?#?#?#?#?#? 1,3,1,6",
        "????.#...#... 4,1,1",
        "????.######..#####. 1,6,5",
        "?###???????? 3,2,1",
    ]


@pytest.fixture
def ex_input1(input_):
    expected = sum([1, 4, 1, 1, 4, 10])
    return input_, expected


@pytest.mark.parametrize(
    ["line", "expected"],
    [
        (".#.#.##..###", [1, 1, 2, 3]),
        ("#.#.##..###.", [1, 1, 2, 3]),
        (".##..##..###..", [2, 2, 3]),
    ],
)
def test_make_test_list(line, expected):
    result = soln.make_test_list(line)
    assert result == expected


@pytest.mark.parametrize(
    ["data", "expected"],
    [
        (["???.### 1,1,3"], 1),
        ([".??..??...?##. 1,1,3"], 4),
        (["?#?#?#?#?#?#?#? 1,3,1,6"], 1),
        (["????.#...#... 4,1,1"], 1),
    ],
)
def test_main_short(data, expected):
    result = soln.main_part1(data)

    assert result == expected


def test_main(ex_input1):
    data, expected = ex_input1
    result = soln.main_part1(data)

    assert result == expected
