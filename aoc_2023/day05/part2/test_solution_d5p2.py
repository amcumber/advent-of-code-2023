import pytest
from aoc_2023.day05.day5 import get_maps

from aoc_2023.day05.part2.solution_d5p2 import (
    get_path_names,
    main,
    parse_seeds,
    get_seed2loc,
    reverse_maps,
    get_loc2seed,
    ALMANAC,
    REV_ALMANAC,
)


@pytest.fixture
def example_input():
    return [
        "seeds: 79 14 55 13",
        "",
        "seed-to-soil map:",
        "50 98 2",
        "52 50 48",
        "",
        "soil-to-fertilizer map:",
        "0 15 37",
        "37 52 2",
        "39 0 15",
        "",
        "fertilizer-to-water map:",
        "49 53 8",
        "0 11 42",
        "42 0 7",
        "57 7 4",
        "",
        "water-to-light map:",
        "88 18 7",
        "18 25 70",
        "",
        "light-to-temperature map:",
        "45 77 23",
        "81 45 19",
        "68 64 13",
        "",
        "temperature-to-humidity map:",
        "0 69 1",
        "1 0 69",
        "",
        "humidity-to-location map:",
        "60 56 37",
        "56 93 4",
    ]


@pytest.fixture
def loc_and_seed():
    return [(81, 79), (57, 55)]


@pytest.fixture
def expected_seeds():
    return [79, 14, 55, 13]


@pytest.fixture
def expected_seed_ranges():
    return [(79, 14), (55, 13)]


@pytest.fixture
def expected_result():
    return {"seed": 82, "location": 46}


def expected_keys():
    return [
        "seed-to-soil",
        "soil-to-fertilizer",
        "fertilizer-to-water",
        "water-to-light",
        "light-to-temperature",
        "temperature-to-humidity",
        "humidity-to-location",
    ]


def expected_rev_keys():
    return [
        "location-to-humidity",
        "humidity-to-temperature",
        "temperature-to-light",
        "light-to-water",
        "water-to-fertilizer",
        "fertilizer-to-soil",
        "soil-to-seed",
    ]


@pytest.fixture
def expected_formatted_seeds():
    return [range(79, 79 + 14), range(55, 55 + 13)]


def test_parse_seeds(expected_seeds, expected_formatted_seeds):
    """Seed parsing is expected to generate a range of seed values"""
    result = parse_seeds(expected_seeds)
    for r, e in zip(result, expected_formatted_seeds):
        assert r == e


def test_rev_almanac():
    expected = {v: k for k, v in ALMANAC.items()}
    assert REV_ALMANAC == expected


@pytest.mark.parametrize(
    ["is_reversed", "expected"],
    [
        (False, expected_keys()),
        (True, expected_rev_keys()),
    ],
)
def test_path_names(is_reversed, expected):
    result = get_path_names(is_reversed)
    assert all([e in result for e in expected])


def test_get_seed2loc(loc_and_seed, example_input):
    maps = get_maps(example_input)
    for loc, seed in loc_and_seed:
        expected = loc
        result = get_seed2loc(seed, maps)
        assert result == expected


def test_get_loc2seed(loc_and_seed):
    maps = get_maps(example_input)
    rev_maps = reverse_maps(maps)
    for loc, seed in loc_and_seed:
        expected = seed
        result = get_loc2seed(loc, rev_maps)
        assert result == expected


def test_main(example_input, expected_result):
    """example solution is seed 82 -> location 46"""
    result = main(example_input)
    assert result["seed"] == expected_result["seed"], "Failed at seed"
    assert result["location"] == expected_result["location"], "Failed at location"
