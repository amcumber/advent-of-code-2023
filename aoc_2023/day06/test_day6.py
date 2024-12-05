import pytest
from aoc_2023.day06.day6 import (
    BoatRace,
    get_n_taus_above_record,
    get_races,
    parse_dists_p1,
    parse_times_p1,
)


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


def test_get_matches(
    example_input, example_match1, example_match2, example_match3
):
    expected = [example_match1, example_match2, example_match3]
    result = get_races(example_input, parse_times_p1, parse_dists_p1)
    for r, e in zip(result, expected):
        r == e


@pytest.mark.parametrize(
    ["tau", "expected_dist", "boat_race"],
    [
        (0, 0, BoatRace(7, 9)),
        (1, 6, BoatRace(7, 9)),
        (2, 10, BoatRace(7, 9)),
        (3, 12, BoatRace(7, 9)),
        (4, 12, BoatRace(7, 9)),
        (5, 10, BoatRace(7, 9)),
        (6, 6, BoatRace(7, 9)),
        (7, 0, BoatRace(7, 9)),
    ],
)
def test_run_race(tau, expected_dist, boat_race):
    result = boat_race.run_race(tau)
    assert result == expected_dist


@pytest.mark.parametrize(
    ["boat_race", "expected"],
    [
        (BoatRace(7, 9), 3.5),
        (BoatRace(15, 40), 7.5),
    ],
)
def test_optimal_tau(boat_race, expected):
    result = boat_race.get_optimal_tau()
    assert result == expected


@pytest.mark.parametrize(
    ["boat_race", "expected"],
    [
        (BoatRace(7, 9), 4),
        (BoatRace(15, 40), 8),
        (BoatRace(30, 200), 9),
    ],
)
def test_get_n_taus_above_record(boat_race, expected):
    taus = boat_race.get_record_taus()
    opt_tau = boat_race.get_optimal_tau()
    results = get_n_taus_above_record(taus, opt_tau)
    assert results == expected
