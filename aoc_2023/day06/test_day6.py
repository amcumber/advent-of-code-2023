import pytest

from aoc_2023.day06.day6 import BoatRace, get_races


@pytest.fixture
def example_input():
    return [
        "Time:      7  15   30",
        "Distance:  9  40  200",
    ]


@pytest.fixture
def example_match1():
    return BoatRace(t=7, d=9)


@pytest.fixture
def example_match2():
    return BoatRace(t=15, d=40)


@pytest.fixture
def example_match3():
    return BoatRace(t=30, d=200)


def test_get_matches(example_input, example_match1, example_match2, example_match3):
    expected = [example_match1, example_match2, example_match3]
    result = get_races(example_input)
    for r, e in zip(result, expected):
        r == e
