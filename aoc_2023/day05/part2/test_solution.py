import pytest

from aoc_2023.day05.test_day5 import example_input, expected_seeds
from aoc_2023.day05.part2.solution import main, parse_seeds


@pytest.fixture
def expected_result():
    return {"seed": 82, "location": 46}


@pytest.fixture
def expected_formatted_seeds():
    return [range(79, 79 + 14), range(55, 55 + 13)]


def test_parse_seeds(expected_seeds, expected_formatted_seeds):
    """Seed parsing is expected to generate a range of seed values"""
    result = parse_seeds(expected_seeds)
    for r, e in zip(result, expected_formatted_seeds):
        assert r == e


def test_main(example_input, expected_result):
    """example solution is seed 82 -> location 46"""
    result = main(example_input)
    assert result["seed"] == expected_result["seed"], "Failed at seed"
    assert result["location"] == expected_result["location"], "Failed at location"
