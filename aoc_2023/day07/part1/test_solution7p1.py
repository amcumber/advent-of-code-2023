import sys
from pathlib import Path

import pytest

if __name__ == "__main__":
    sys.path.append(str(Path(__file__).parent.resolve() / "../../.."))

from aoc_2023.core import read_input
from aoc_2023.day07.part1.solution7p1 import calc_result, main


@pytest.fixture
def exp_input():
    return [
        "32T3K 765",
        "T55J5 684",
        "KK677 28",
        "KTJJT 220",
        "QQQJA 483",
    ]


@pytest.fixture
def exp_total():
    return 6440


@pytest.fixture
def exp_main_result():
    return [
        (1, 765),
        (4, 684),
        (3, 28),
        (2, 220),
        (5, 483),
    ]


def test_main(exp_input, exp_main_result):
    result = main(exp_input)
    for (r_rank, r_wager), (e_rank, e_wager) in zip(result, exp_main_result):
        assert r_rank == e_rank, "Failed rank"
        assert r_wager == e_wager, "Failed wager"


def test_calc_result(exp_input, exp_total):
    val = main(exp_input)
    result = calc_result(val)
    assert result == exp_total, "Failed total"
