import sys
from pathlib import Path

import pytest

if __name__ == "__main__":
    sys.path.append(str(Path(__file__).parent.resolve() / "../../.."))

from aoc_2023.day07.day7 import CamelHand, HandType, calc_result
from aoc_2023.day07.part2.solution7p2 import CARD_RANK_7P2, main


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
    return 5905


@pytest.fixture
def exp_main_result():
    return [
        (1, 765),
        (3, 684),
        (2, 28),
        (5, 220),
        (4, 483),
    ]


@pytest.mark.parametrize(
    ["hand", "expected"],
    [
        ("12345", HandType.high_card),
        ("1234J", HandType.one_pair),
        ("32T3K", HandType.one_pair),
        ("32J3K", HandType.three_of_a_kind),
        ("KK677", HandType.two_pair),
        ("JKJTT", HandType.four_of_a_kind),
        ("QQJAA", HandType.full_house),
        ("T55J5", HandType.four_of_a_kind),
        ("QQQJA", HandType.four_of_a_kind),
        ("Q7QQA", HandType.three_of_a_kind),
        ("JJJQA", HandType.four_of_a_kind),
        ("QQQAA", HandType.full_house),
        ("JJJAA", HandType.five_of_a_kind),
        ("AAAA9", HandType.four_of_a_kind),
        ("AAAAJ", HandType.five_of_a_kind),
        ("JJJJ9", HandType.five_of_a_kind),
        ("JJJJJ", HandType.five_of_a_kind),
        ("AAAAA", HandType.five_of_a_kind),
    ],
)
def test_hand(hand, expected):
    handed = CamelHand(hand, card_rank=CARD_RANK_7P2, wild_card="J")
    result = handed.get_hand_type()
    assert result == expected, "failed type"


def test_main(exp_input, exp_main_result):
    result = main(exp_input)
    for (r_rank, r_wager), (e_rank, e_wager) in zip(result, exp_main_result):
        assert r_rank == e_rank, "Failed rank"
        assert r_wager == e_wager, "Failed wager"


def test_calc_result(exp_input, exp_total):
    val = main(exp_input)
    result = calc_result(val)
    assert result == exp_total, "Failed total"
