import re
from dataclasses import dataclass
from typing import Any, NamedTuple

AlmanacEntryType = tuple[int, int, int]
DestSourceTupleType = tuple[int, int]
SparseMapType = Any


class AlmanacEntry(NamedTuple):
    dest: int
    source: int
    rng: int

    def reverse(self) -> AlmanacEntryType:
        return self.__class__(self.source, self.dest, self.rng)

    def __add__(self, value: int, /):
        return self.__class__(self.source + value, self.dest + value, self.rng)

    def __sub__(self, value: int, /):
        return self.__class__(self.source - value, self.dest - value, self.rng)


class DestSourceTuple(NamedTuple):
    dest: int
    source: int

    def reverse(self) -> DestSourceTupleType:
        return self.__class__(self.source, self.dest)


@dataclass
class SparseMap:
    map_info: list[AlmanacEntry]

    def is_in(self, value: int) -> tuple[bool, int]:
        for loc, (_, source, rng) in enumerate(self.map_info):
            if value >= source and value < source + rng:
                return True, loc
        return False, None

    def get(self, key, default=None):
        if default is None:
            default = key
        is_map, loc = self.is_in(key)
        if not is_map:
            return default
        dest, source, _ = self.map_info[loc]
        idx = key - source
        return dest + idx

    def reverse(self) -> SparseMapType:
        """Return a SparseMap with source and dest reversed"""
        return self.__class__([entry.reverse() for entry in self.map_info])

    def min(self) -> list[DestSourceTuple]:
        """Return a named tuple with with minimum sources and destinations"""
        return [DestSourceTuple(dest, source) for dest, source, _ in self.map_info]

    def max(self) -> list[DestSourceTuple]:
        """Return a named tuple with with maximum sources and destinations"""
        return [
            DestSourceTuple(dest + rng - 1, source + rng - 1)
            for dest, source, rng in self.map_info
        ]

    def get_nodes(self) -> list[DestSourceTuple]:
        """Get edges of the specified mapping ranges in map"""
        nodes = []
        nodes.extend(mins := self.min())
        nodes.extend(maxes := self.max())
        for (mini_d, mini_s), (maxi_d, maxi_s) in zip(mins, maxes):
            nodes.append(DestSourceTuple(mini_d - 1, mini_s - 1))
            nodes.append(DestSourceTuple(maxi_d + 1, maxi_s + 1))
        nodes.sort(key=lambda x: x[0])
        return nodes


def walk_almanac(
    almanac: dict[str, str],
    start: int,
    maps: dict[str, SparseMap],
    start_name: str = "seed",
) -> tuple[list[int], list[str]]:
    """Walk almanac from start_name to end based on almanac and maps data

    Parameters
    ----------
    almanac: dict[str, str]
        1-1 name connections to generate keys in maps( e.g. {'seed': 'soil'})
    start: int
        start value
    maps: dict[str, SparseMap]
        maps data with keys x-to-y (e.g. seed-to-soil)
    start_name : str
        start name to start walking maps, default is 'seed'

    Returns
    -------
    key_path : list[int]
        values
    name_path : list[str]
        names
    """
    this_key = start_name
    val = start
    key_path = [start]
    name_path = [start_name]
    while True:
        next_key = almanac.get(this_key, this_key)
        if next_key == this_key:
            break
        map_name = _get_map_name(this_key, next_key)
        map_ = maps[map_name]
        val = map_.get(val, val)
        key_path.append(val)
        name_path.append(next_key)
        this_key = next_key
    return key_path, name_path


def _get_map_name(key, val):
    return f"{key}-to-{val}"


def populate_almanac_links(
    almanac: dict[str, str],
    start_name: str,
) -> list[str]:
    """Populate a sequence of map keys that will walk the provided almanac"""
    name_path = []
    this_key = start_name
    while True:
        next_key = almanac.get(this_key, this_key)
        map_name = _get_map_name(this_key, next_key)
        if next_key == this_key:
            break
        name_path.append(map_name)
        this_key = next_key
    return name_path


def _parse_str_arr(array: str) -> list[int]:
    m = re.compile(r"\s+")
    return [int(ele) for ele in m.split(array.strip())]


def get_seeds(lines: list[str]) -> list[int]:
    pattern = r"seeds:"
    m = re.compile(pattern)
    for line in lines:
        if m.match(line):
            break
    return _parse_str_arr(line.strip(pattern))


def get_maps(lines: list[str]) -> dict[str, SparseMap]:
    pattern = r"map:"
    m = re.compile(pattern)
    maps = {}

    map_flag = False
    map_info = []
    map_name = ""
    for line in lines:
        if not len(line.strip()):
            if map_info:
                maps[map_name] = _parse_map(map_info)
            map_flag = False
            map_info = []
            map_name = ""
        elif map_flag:
            map_info.append(AlmanacEntry(*_parse_str_arr(line)))

        elif m.search(line):
            map_flag = True
            map_name = line.strip(pattern).strip()
    if map_info:
        maps[map_name] = _parse_map(map_info)

    return maps


def _parse_map(map_info: list[tuple[int, int, int]]) -> SparseMap:
    """Parse map info a list of key start, value start and range size values"""
    return SparseMap(map_info)
