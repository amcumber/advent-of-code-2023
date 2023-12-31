import pytest

from aoc_2023.day07.day7 import main


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
def exp_rank():
    return [1, 4, 3, 2, 5]


@pytest.fixture
def exp_wager():
    return [765, 684, 28, 220, 483]


@pytest.fixture
def exp_score():
    return [765 * 1, 220 * 2, 28 * 3, 684 * 4, 483 * 5]


@pytest.fixture
def exp_hand_rank():
    ks = list(reversed("AKQJT987654321"))
    return {k: v for k, v in zip(ks, range(1, len(ks) + 1))}


def test_main(exp_input, exp_score):
    result = main(exp_input)
    assert sum(result) == sum(exp_score)
