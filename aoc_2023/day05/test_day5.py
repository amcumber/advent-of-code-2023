import pytest

from aoc_2023.day05.day5 import get_maps, get_seeds


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
def expected_seeds():
    return [79, 14, 55, 13]


@pytest.fixture
def expected_seed2soil_sample():
    return {
        98: 50,
        99: 51,
    }


def test_get_seeds(expected_seeds):
    results = get_seeds(example_input())
    assert results == expected_seeds


def test_seed2soil_map(expected_seed2soil_sample):
    maps = get_maps(example_input())
    results = maps["seed-to-soil"]
    for key, expected in expected_seed2soil_sample.items():
        r = results.get(key, key)
        assert r == expected


@pytest.mark.parametrize(
    ["seed", "soil"],
    [
        (79, 81),
        (14, 14),
        (55, 57),
        (13, 13),
    ],
)
def test_seed2soil_inputs(seed, soil):
    maps = get_maps(example_input())
    results = maps["seed-to-soil"]
    result = results.get(seed, seed)
    assert result == soil


@pytest.mark.parametrize(
    ["soil", "fertilizer"],
    [
        (81, 81),
        (14, 53),
        (57, 57),
        (13, 52),
    ],
)
def test_soil2fertilizer_inputs(soil, fertilizer):
    maps = get_maps(example_input())
    results = maps["soil-to-fertilizer"]
    result = results.get(soil, soil)
    assert result == fertilizer


@pytest.mark.parametrize(
    ["fertilizer", "water"],
    [
        (81, 81),
        (53, 49),
        (57, 53),
        (52, 41),
    ],
)
def test_fert2water_inputs(fertilizer, water):
    maps = get_maps(example_input())
    results = maps["fertilizer-to-water"]
    result = results.get(fertilizer, fertilizer)
    assert result == water


@pytest.mark.parametrize(
    ["water", "light"],
    [
        (81, 74),
        (49, 42),
        (53, 46),
        (41, 34),
    ],
)
def test_water2light_inputs(water, light):
    maps = get_maps(example_input())
    results = maps["water-to-light"]
    result = results.get(water, water)
    assert result == light


@pytest.mark.parametrize(
    ["light", "temperature"],
    [
        (74, 78),
        (42, 42),
        (46, 82),
        (34, 34),
    ],
)
def test_light2temp_inputs(light, temperature):
    maps = get_maps(example_input())
    results = maps["light-to-temperature"]
    result = results.get(light, light)
    assert result == temperature


@pytest.mark.parametrize(
    ["temperature", "humidity"],
    [
        (78, 78),
        (42, 43),
        (82, 82),
        (34, 35),
    ],
)
def test_temp2humid_inputs(temperature, humidity):
    maps = get_maps(example_input())
    results = maps["temperature-to-humidity"]
    result = results.get(temperature, temperature)
    assert result == humidity


@pytest.mark.parametrize(
    ["humidity", "location"],
    [
        (78, 82),
        (43, 43),
        (82, 86),
        (35, 35),
    ],
)
def test_humid2loc_inputs(humidity, location):
    maps = get_maps(example_input())
    results = maps["humidity-to-location"]
    result = results.get(humidity, humidity)
    assert result == location
