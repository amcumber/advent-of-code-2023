import pytest

from aoc_2023.day02.part1.solution import (
    evaluate_game,
    get_game_maxes,
    parse_draw,
    parse_line,
    parse_sets,
)


@pytest.fixture
def example_line():
    return (
        """Game 1: 7 green, 14 red, 5 blue; 8 red, 4 green; 6 green, 18 red, 9 blue"""
    )


@pytest.fixture
def example_set():
    return """7 green, 14 red, 5 blue; 8 red, 4 green; 6 green, 18 red, 9 blue"""


@pytest.fixture
def example_draw():
    return "7 green, 14 red, 5 blue"


def test_parse_draw(example_draw):
    expected = {"green": 7, "red": 14, "blue": 5}
    result = parse_draw(example_draw)
    for key, val in result.items():
        assert key in expected, f"Failed Key: {key}"
        assert val == expected.get(key), f"Failed Value: {val}"


def test_parse_sets(example_set):
    expected = [
        {"green": 7, "red": 14, "blue": 5},
        {"red": 8, "green": 4},
        {"green": 6, "red": 18, "blue": 9},
    ]
    result = parse_sets(example_set)
    for idx, (r, e) in enumerate(zip(result, expected)):
        for key, val in r.items():
            assert key in e, f"Failed Key: {idx}:{key}"
            assert val == e.get(key), f"Failed Value: {idx}:{val}"


def test_parse_game(example_line):
    expected = {
        1: [
            {"green": 7, "red": 14, "blue": 5},
            {"red": 8, "green": 4},
            {"green": 6, "red": 18, "blue": 9},
        ]
    }
    result = parse_line(example_line)
    for game_idx, payload in result.items():
        assert game_idx in expected, f"Failed Game ID: {game_idx}"
        for idx, (r, e) in enumerate(zip(payload, expected[game_idx])):
            for key, val in r.items():
                assert key in e, f"Failed Key: {idx}:{key}"
                assert val == e.get(key), f"Failed Value: {idx}:{val}"


def test_get_game_maxes():
    game = {
        1: [
            {"green": 7, "red": 14, "blue": 5},
            {"red": 8, "green": 4},
            {"green": 6, "red": 18, "blue": 9},
        ]
    }
    expected = {"green": 7, "red": 18, "blue": 9}
    result = get_game_maxes(game)
    for color, val in result.items():
        assert color in expected, "Failed Color"
        assert expected[color] == val, "Failed Value comparison"


def test_evaluate_game_true():
    game = {
        1: [
            {"green": 7, "red": 14, "blue": 5},
            {"red": 8, "green": 4},
            {"green": 6, "red": 18, "blue": 9},
        ]
    }
    rule = {"green": 10, "red": 20, "blue": 10}
    result = evaluate_game(game, rule)
    assert result == True, "Failed evaluation"


@pytest.mark.parametrize(
    "rule",
    [
        {"green": 2, "red": 20, "blue": 10},
        {"green": 10, "blue": 10},
    ],
)
def test_evaluate_game_false(rule):
    game = {
        1: [
            {"green": 7, "red": 14, "blue": 5},
            {"red": 8, "green": 4},
            {"green": 6, "red": 18, "blue": 9},
        ]
    }
    result = evaluate_game(game, rule)
    assert result == False, "Failed evaluation"
