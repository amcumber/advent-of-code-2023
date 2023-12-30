from functools import reduce

import pytest

from aoc_2023.day06.day6 import BoatRace
from aoc_2023.day06.part1.solution_d6p1 import get_n_taus_above_record, main


@pytest.fixture
def example_input():
    return [
        "Time:      7  15   30",
        "Distance:  9  40  200",
    ]


@pytest.fixture
def expected_main_result():
    return [4, 8, 9]


@pytest.fixture
def expected_solution():
    return 288


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


def test_main(example_input, expected_main_result, expected_solution):
    result = main(example_input)
    assert result == expected_main_result
    assert reduce(lambda x, y: x * y, result) == expected_solution
