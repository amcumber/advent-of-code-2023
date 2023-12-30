import math
import re
from dataclasses import dataclass
from functools import reduce
from typing import Callable, Iterable

from aoc_2023.core import (
    AOCAttributeError,
    AOCValueError,
    concat_str_int,
    parse_line,
    parse_str_arr,
)


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

    def run_race(self, tau: int) -> int:
        """Run a race with tau, the time spent holding down the boat

        v = tau
        d = v * (t-tau)
        d = tau * (t-tau)
        d = t*tau - tau**2

        Parameters
        ----------
        tau : int
            the time spent holding down the boat

        Returns
        -------
        int
            boat distance
        """
        return self.t * tau - tau**2

    def get_optimal_tau(self) -> float:
        """Get optimal tau, where the maximum distance can be achieved

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
        return self.t / 2

    def get_record_taus(self) -> tuple[float, float]:
        """Get tau value for the specified record (parameter d)
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

        r_root = _left_root(a := -1, b := self.t, c := -self.d)
        l_root = _right_root(a, b, c)

        # if isinstance(l_root, complex):
        #     return math.nan, r_root
        # elif isinstance(r_root, complex):
        #     return l_root, math.nan
        if math.nan in (l_root, r_root):
            raise AOCValueError("Complex roots found in solution")
        return l_root, r_root


def get_n_taus_above_record(record_tau: tuple[float, float], opt_tau: float) -> int:
    low, high = record_tau
    # correction for equal values
    low += 1e-6
    high -= 1e-6
    return len(range(math.ceil(low), math.ceil(high)))


def calc_result(result: list[int]):
    return reduce(lambda x, y: x * y, result)


def parse_times_p1(input_data: Iterable[str]) -> list[int]:
    """Part 1 time parser"""
    pattern = "Time:"

    times = []
    for line in input_data:
        str_arr = parse_line(line, pattern)
        times.extend(parse_str_arr(str_arr))
    return times


def parse_dists_p1(input_data: Iterable[str]) -> list[int]:
    """Part 1 distance parser"""
    pattern = "Distance:"

    distances = []
    for line in input_data:
        str_arr = parse_line(line, pattern)
        distances.extend(parse_str_arr(str_arr))
    return distances


def parse_times_p2(input_data: Iterable[str]) -> list[int]:
    """Part 2 time parser"""
    pattern = "Time:"

    times = []
    for line in input_data:
        str_arr = parse_line(line, pattern)
        times.extend(concat_str_int(str_arr))
    return times


def parse_dists_p2(input_data: Iterable[str]) -> list[int]:
    """Part 2 distance parser"""
    pattern = "Distance:"

    distances = []
    for line in input_data:
        str_arr = parse_line(line, pattern)
        distances.extend(concat_str_int(str_arr))
    return distances


def get_races(
    input_data: Iterable[str],
    time_parser,
    dist_parser,
) -> list[BoatRace]:
    times = time_parser(input_data)
    dists = dist_parser(input_data)
    return [BoatRace(t, d) for t, d in zip(times, dists)]
