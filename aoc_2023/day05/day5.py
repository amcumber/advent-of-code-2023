import re
from dataclasses import dataclass

AlmanacEntry = tuple[int, int, int]


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


def walk_almanac(
    almanac: dict[str, str], start: int, maps: dict[dict[int, int]], start_name="seed"
) -> tuple[list[int], list[str]]:
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


def _parse_str_arr(array: str) -> list[int]:
    m = re.compile(r"\s+")
    return [int(ele) for ele in m.split(array.strip())]


def get_seeds(lines: list[str]):
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
            map_info.append(tuple(_parse_str_arr(line)))

        elif m.search(line):
            map_flag = True
            map_name = line.strip(pattern).strip()
    if map_info:
        maps[map_name] = _parse_map(map_info)

    return maps


def _parse_map(map_info: list[tuple[int, int, int]]) -> SparseMap:
    """Parse map info a list of key start, value start and range size values"""
    return SparseMap(map_info)
