import pytest
from aoc_2023.day04.part2.solution import count_cards, main, score_matches


@pytest.fixture
def example_input():
    return [
        "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
        "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
        "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
        "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
        "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
        "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
    ]


@pytest.fixture
def expected_winners():
    return [
        [41, 48, 83, 86, 17],
        [13, 32, 20, 16, 61],
        [1, 21, 53, 59, 44],
        [41, 92, 73, 84, 69],
        [87, 83, 26, 28, 32],
        [31, 18, 13, 56, 72],
    ]


@pytest.fixture
def expected_cards():
    return [
        [83, 86, 6, 31, 17, 9, 48, 53],
        [61, 30, 68, 82, 17, 32, 24, 19],
        [69, 82, 63, 72, 16, 21, 14, 1],
        [59, 84, 76, 51, 58, 5, 54, 83],
        [88, 30, 70, 12, 93, 22, 82, 36],
        [74, 77, 10, 23, 35, 67, 36, 11],
    ]


@pytest.fixture
def expected_matches():
    return [
        [83, 86, 17, 48],
        [61, 32],
        [21, 1],
        [84],
        [],
        [],
    ]


@pytest.fixture
def expected_scores():
    return [4, 2, 2, 1, 0, 0]


@pytest.fixture
def expected_n_cards():
    return [1, 2, 4, 8, 14, 1]


def test_count_cards(expected_scores, expected_n_cards):
    result = count_cards(expected_scores)
    for r, e in zip(result, expected_n_cards):
        assert r == e


def test_score_matches(expected_matches, expected_scores):
    result = [score_matches(matches) for matches in expected_matches]
    for r, e in zip(result, expected_scores):
        assert r == e


def test_main(example_input):
    # expected = sum(l := [1 * 4, 2 * 2, 4 * 2, 8 * 1, 14 * 0, 0]) + len(l)
    expected = 30
    result = main(example_input)
    assert sum(result) == expected
