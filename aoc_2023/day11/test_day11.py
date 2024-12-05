import pytest

from . import day11


@pytest.fixture
def input_():
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


@pytest.fixture
def ex_part1(input_):
    expected = 374
    return input_, expected


def test_find_gals(input_):
    expected = [
        (0, 3),
        (1, 7),
        (2, 0),
        (4, 6),
        (5, 1),
        (6, 9),
        (8, 7),
        (9, 0),
        (9, 4),
    ]
    result = day11.find_gals(input_)
    for r, e in zip(expected, result):
        assert r == e

def test_find_wormholes(input_):
    expected = [[3, 7], [2, 5, 8]]
    gals = day11.find_gals(input_)
    result = day11.find_wormholes(gals)
    for r, e in zip(expected, result):
        assert r == e

def test_part1(ex_part1):
    input_, expected = ex_part1
    result = day11.main_part1(input_)
    assert result == expected

@pytest.mark.parametrize(['age', 'expected'], [(2, 374), (10, 1030), (100, 8410)])
def test_part2(input_, age, expected):
    result = day11.main_part2(input_, age)
    assert result == expected
