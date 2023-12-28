"""solution for part 2 day 5"""
import sys
from pathlib import Path
from typing import Any, Iterable

if __name__ == "__main__":
    sys.path.append(str(Path(__file__).parent.resolve() / "../../.."))

from aoc_2023.core import read_input, AOCKeyError
from aoc_2023.day05.day5 import (
    get_maps,
    get_seeds,
    populate_almanac_links,
    walk_almanac,
    SparseMap,
)

ALMANAC = {
    "seed": "soil",
    "soil": "fertilizer",
    "fertilizer": "water",
    "water": "light",
    "light": "temperature",
    "temperature": "humidity",
    "humidity": "location",
}
START_NAME = "seed"
REV_NAME = "location"

Key = Any
Value = Any
REV_ALMANAC = {v: k for k, v in ALMANAC.items()}


def get_reversed_maps(maps: dict[str, SparseMap]) -> dict[str, SparseMap]:
    """Reverse maps dictionary"""
    new_maps = {}
    for key, map_ in maps.items():
        a, to_, b = key.split("-")
        new_key = "-".join((b, to_, a))
        new_maps[new_key] = map_.reverse()
    return new_maps


def _get_x2y(
    x: int,
    x_name: str,
    y_name: str,
    maps: dict[str, SparseMap],
    almanac: dict[str, str],
):
    """Walk a location to seed using a reversed_maps dict"""
    if not (y_name in almanac or y_name in almanac.values()):
        raise AOCKeyError("Bad y_name refer to almanac for valid values")
    values, destinations = walk_almanac(almanac, x, maps, start_name=x_name)
    val2dest = {d: val for val, d in zip(values, destinations)}
    return val2dest[y_name]


def get_seed2loc(seed: int, maps: dict[str, SparseMap]):
    """Get a location based on seed num"""
    return _get_x2y(seed, START_NAME, REV_NAME, maps, ALMANAC)


def get_loc2seed(loc: int, reversed_maps: dict[str, SparseMap]):
    """Walk a location to seed using a reversed_maps dict"""
    return _get_x2y(loc, REV_NAME, START_NAME, reversed_maps, REV_ALMANAC)


def get_link_names(is_reversed=False) -> list[str]:
    """Walk a location to seed using a reversed_maps dict"""
    if is_reversed:
        return populate_almanac_links(REV_ALMANAC, REV_NAME)

    return populate_almanac_links(ALMANAC, START_NAME)


def map_node_edges(
    reverse_maps: dict[str, SparseMap]
) -> dict[str, list[tuple[int, int]]]:
    """For each end of the reversed_map"""


def get_paths(
    seeds: Iterable[int], maps: list[str, SparseMap]
) -> dict[int, dict[str, int]]:
    paths = {}
    for seed in seeds:
        path, _ = walk_almanac(ALMANAC, seed, maps, start_name=START_NAME)
        paths[seed] = path

    return paths


def find_min_loc(paths: dict[int, list[int]]):
    """find minimum location"""
    return
    loc2seed = {}
    for seed, path in paths.items():
        loc2seed[path[-1]] = seed
    min_loc = min(loc2seed.keys())
    return min_loc, loc2seed[min_loc]


def parse_seeds(seeds: list[int]) -> list[range]:
    seed_ranges = []
    for idx2, start in enumerate(seeds[::2]):
        s_range = seeds[2 * idx2 + 1]
        seed_ranges.append(range(start, start + s_range))
    return seed_ranges


def main(input_data: list[str]):
    """Run solution"""
    seeds = get_seeds(input_data)
    seed_ranges = parse_seeds(seeds)
    maps = get_maps(input_data)
    paths = get_paths(seed_ranges, maps)
    min_loc, min_seed = find_min_loc(paths)
    return min_loc, min_seed, paths


if __name__ == "__main__":
    input_file = Path(__file__).parent.parent / "input.txt"
    input_data = read_input(input_file)
    result, *_ = main(input_data)

    output_file = Path(__file__).parent / "result.txt"
    with open(output_file, "w") as fh:
        fh.write(str(result))
    print(f"The sum is {result}")
