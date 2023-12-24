import re
from dataclasses import dataclass
from typing import Iterable


class MatchError(Exception):
    "Base error"


class MatchAttributeError(MatchError):
    "Attribute error"


@dataclass
class Match:
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
            raise MatchError("Cannot compare unlike types")
        if self.t != __value.t or self.d != __value.d:
            return False
        return True

def _parse_line(line: str) -> list[list[int]]:
    vals = line.split(":")[1].strip()
    return tuple(_parse_str_arr(arr) for arr in (winner_str, card_str))

def _parse_times(input_data: Iterable[str]) -> list[int]:
    pattern = 'Times :'

    _parse_line(pattern)
    for line in input_data:
        
        


def _parse_dists(input_data: Iterable[str]) -> list[int]:
    ...


def get_matches(input_data: Iterable[str]) -> list[Match]:
    times = _parse_times(input_data)
    dists = _parse_dists(input_data)
    return [Match(t, d) for t, d in zip(times, dists)]
