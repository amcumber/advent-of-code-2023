import math
import re
from dataclasses import dataclass
from typing import Iterable

from aoc_2023.core import AOCAttributeError, parse_line, parse_str_arr


@dataclass
class BoatRace:
    """Boat race match for day 6
    Properties
    ----------
    t: int
        time
    d: int
        distance
    """

    t: int
    d: int

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value.__class__, self.__class__):
            raise AOCAttributeError("Cannot compare unlike types")
        if self.t != __value.t or self.d != __value.d:
            return False
        return True


def parse_times(input_data: Iterable[str]) -> list[int]:
    pattern = "Time:"

    times = []
    for line in input_data:
        str_arr = parse_line(line, pattern)
        times.extend(parse_str_arr(str_arr))
    return times


def parse_dists(input_data: Iterable[str]) -> list[int]:
    pattern = "Distance:"

    distances = []
    for line in input_data:
        str_arr = parse_line(line, pattern)
        distances.extend(parse_str_arr(str_arr))
    return distances


def get_races(input_data: Iterable[str]) -> list[BoatRace]:
    times = parse_times(input_data)
    dists = parse_dists(input_data)
    return [BoatRace(t, d) for t, d in zip(times, dists)]


def get_optimal_tau(race: BoatRace) -> float:
    """TBR
    v = tau
    d = v * (t-tau)
    d = tau * (t-tau)
    d = t*tau - tau**2

    dd/dtau = t - 2*tau
    0 = t - 2*tau
    2*tau = t
    tau = t/2

    tau = (-b +/- sqrt(b**2 - 4*a*c)) / (2*a)
    tau = (-(t) +/- sqrt((t)**2 - 4*(t)*(-d))) / (2*(-1))
    tau = (-t +/- sqrt(t**2 + 4*t*d)) / (-2))
    | t   | tau | t-tau | v   | d   |
    | --- | --- | ----- | --- | --- |
    | 7   | 1   | 6     | 1   | 6   |
    | 7   | 2   | 5     | 2   | 10  |
    | 7   | 3   | 4     | 3   | 12  |
    | 7   | 4   | 3     | 4   | 12  |
    | 7   | 5   | 2     | 5   | 10  |
    | 7   | 6   | 1     | 6   | 6   |
    """
    return race.t / 2


def get_record_tau(race: BoatRace) -> int:
    """TBR
    v = tau
    d = v * (t-tau)
    d = tau * (t-tau)
    d = t*tau - tau**2

    tau = (-b +/- sqrt(b**2 - 4*a*c)) / (2*a)
    tau = (-(t) +/- sqrt((t)**2 - 4*(t)*(-d))) / (2*(-1))
    tau = (-t +/- sqrt(t**2 + 4*t*d)) / (-2))

    a = -1, b = t, c = -d
    """

    def _left_root(a, b, c):
        return (-b - _get_det(a, b, c)) / (2 * a)

    def _right_root(a, b, c):
        return (-b + _get_det(a, b, c)) / (2 * a)

    def _get_det(a, b, c):
        det = b**2 - 4 * a * c
        if det < 0:
            return complex(0, math.abs(det))
        return math.sqrt(det)

    l_root = _left_root(a := -1, b := race.t, c := -race.d)
    r_root = _right_root(a, b, c)

    if isinstance(l_root, complex):
        return r_root
    if isinstance(r_root, complex):
        return l_root
    return int(max(l_root, r_root))
