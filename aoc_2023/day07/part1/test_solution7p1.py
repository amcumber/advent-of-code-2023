import sys
from pathlib import Path

import pytest

if __name__ == "__main__":
    sys.path.append(str(Path(__file__).parent.resolve() / "../../.."))

from aoc_2023.day07.day7 import CamelHand, HandType
from aoc_2023.day07.part1.solution7p1 import CARD_RANK_7P1, calc_result, main


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


@pytest.mark.parametrize(
    ["hand", "expected"],
    [
        ("12345", HandType.high_card),
        ("1234J", HandType.high_card),
        ("32T3K", HandType.one_pair),
        ("32J3K", HandType.one_pair),
        ("KK677", HandType.two_pair),
        ("JKJTT", HandType.two_pair),
        ("QQJAA", HandType.two_pair),
        ("T55J5", HandType.three_of_a_kind),
        ("QQQJA", HandType.three_of_a_kind),
        ("Q7QQA", HandType.three_of_a_kind),
        ("JJJQA", HandType.three_of_a_kind),
        ("QQQAA", HandType.full_house),
        ("JJJAA", HandType.full_house),
        ("AAAA9", HandType.four_of_a_kind),
        ("AAAAJ", HandType.four_of_a_kind),
        ("JJJJ9", HandType.four_of_a_kind),
        ("JJJJJ", HandType.five_of_a_kind),
        ("AAAAA", HandType.five_of_a_kind),
    ],
)
def test_hand(hand, expected):
    handed = CamelHand(hand, card_rank=CARD_RANK_7P1)
    result = handed.get_hand_type()
    assert (
        result == expected
    ), f"failed type hand: {handed!r}, {result!r} != {expected!r}"


def test_main(exp_input, exp_main_result):
    result = main(exp_input)
    for (r_rank, r_wager), (e_rank, e_wager) in zip(result, exp_main_result):
        assert r_rank == e_rank, "Failed rank"
        assert r_wager == e_wager, "Failed wager"


def test_calc_result(exp_input, exp_total):
    val = main(exp_input)
    result = calc_result(val)
    assert result == exp_total, "Failed total"
