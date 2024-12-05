"""solution for part 2 day 5"""

import sys
from collections import namedtuple
from dataclasses import dataclass
from pathlib import Path
from typing import Any

if __name__ == "__main__":
    sys.path.append(str(Path(__file__).parent.resolve() / "../../.."))

from aoc_2023.core import AOCKeyError, read_input
from aoc_2023.day05.day5 import (
    DestSourceTuple,
    SparseMap,
    get_maps,
    get_seeds,
    populate_almanac_links,
    walk_almanac,
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
MapsType = dict[str, SparseMap]
AlmanacType = dict[str, str]
MapNodeType = dict[str, list[int]]
REV_ALMANAC = {v: k for k, v in ALMANAC.items()}

SeedLoc = namedtuple("SeedLoc", ["seed", "location"])


@dataclass
class SeedRanges:
    seed_ranges: list[range]

    def is_in(self, value: int) -> bool:
        for seed_range in self.seed_ranges:
            if value in seed_range:
                return True
        return False

    def min(self) -> list[int]:
        """Return a list with minimum seeds"""
        return [min(seed_range) for seed_range in self.seed_ranges]

    def max(self) -> list[int]:
        """Return a list with maximum seeds"""
        return [max(seed_range) for seed_range in self.seed_ranges]

    def get_nodes(self) -> list[DestSourceTuple]:
        """Get edges of the seeds mapping ranges in map"""
        nodes = []
        nodes.extend(mins := self.min())
        nodes.extend(maxes := self.max())
        for mini, maxi in zip(mins, maxes):
            nodes.append(mini - 1)
            nodes.append(maxi + 1)
        nodes.sort()
        return nodes


def _get_reversed_maps(maps: MapsType) -> MapsType:
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
    maps: MapsType,
    almanac: AlmanacType,
):
    """Walk a location to seed using a reversed_maps dict"""
    if not (y_name in almanac or y_name in almanac.values()):
        raise AOCKeyError("Bad y_name refer to almanac for valid values")
    values, destinations = walk_almanac(almanac, x, maps, start_name=x_name)
    val2dest = {d: val for val, d in zip(values, destinations)}
    return val2dest[y_name]


def get_seed2loc(seed: int, maps: MapsType):
    """Get a location based on seed num"""
    return _get_x2y(seed, START_NAME, REV_NAME, maps, ALMANAC)


def get_loc2seed(loc: int, reversed_maps: MapsType):
    """Walk a location to seed using a reversed_maps dict"""
    return _get_x2y(loc, REV_NAME, START_NAME, reversed_maps, REV_ALMANAC)


def get_link_names(is_reversed=False) -> list[str]:
    """Walk a location to seed using a reversed_maps dict"""
    if is_reversed:
        return populate_almanac_links(REV_ALMANAC, REV_NAME)

    return populate_almanac_links(ALMANAC, START_NAME)


def _get_node_edges(reversed_maps: MapsType) -> MapNodeType:
    """For each end of the reversed_map"""
    node_edges = {}
    for starting_node, map_ in reversed_maps.items():
        name = starting_node.split("-")[0]
        node_edges[name] = [node.source for node in map_.get_nodes()]
    return node_edges


def _get_nodes2seeds(
    name: str,
    nodes: list[int],
    reversed_maps: MapsType,
) -> list[int]:
    """Take a set of nodes given a node name and map them to seeds"""
    return [
        _get_x2y(node, name, START_NAME, reversed_maps, REV_ALMANAC)
        for node in nodes
    ]


def _map_node_edges2seeds(
    node_edges: MapNodeType, reversed_maps: MapsType
) -> list[int]:
    """Map a set of node_edges to seeds"""
    seeds = []
    for name, nodes in node_edges.items():
        seeds.extend(_get_nodes2seeds(name, nodes, reversed_maps))
    return seeds


# def get_paths(seeds: Iterable[int], maps: MapsType) -> dict[int, dict[str, int]]:
#     paths = {}
#     for seed in seeds:
#         path, _ = walk_almanac(ALMANAC, seed, maps, start_name=START_NAME)
#         paths[seed] = path

#     return paths


def _find_min_loc(seed_map: dict[int, int]) -> tuple[int, int]:
    """find minimum location"""
    loc2seed = {loc: seed for seed, loc in seed_map.items()}
    min_loc = min(loc2seed.keys())
    return min_loc, loc2seed[min_loc]


def parse_seeds(seeds: list[int]) -> SeedRanges:
    seed_ranges = []
    for idx2, start in enumerate(seeds[::2]):
        s_range = seeds[2 * idx2 + 1]
        seed_ranges.append(range(start, start + s_range))
    return SeedRanges(seed_ranges)


def get_key_seeds(seed_ranges: SeedRanges, maps: MapsType) -> list[int]:
    """Find all the key seeds around edges of seed_ranges and map_nodes"""
    seed_nodes = seed_ranges.get_nodes()
    reversed_maps = _get_reversed_maps(maps)

    map_nodes = _get_node_edges(reversed_maps)
    map_seed_nodes = _map_node_edges2seeds(map_nodes, reversed_maps)
    seed_nodes.extend(map_seed_nodes)
    reduced_seeds = list(set(seed_nodes))
    return [seed for seed in reduced_seeds if seed_ranges.is_in(seed)]


def _map_key_seeds(key_seeds: list[int], maps: MapsType) -> dict[int, int]:
    return {seed: get_seed2loc(seed, maps) for seed in key_seeds}


def find_min_seed_from_key_seeds(
    key_seeds: list[int], maps: MapsType
) -> tuple[int, int]:
    seed_map = _map_key_seeds(key_seeds, maps)
    min_loc, min_seed = _find_min_loc(seed_map)
    return {"seed": min_seed, "location": min_loc}


def main(input_data: list[str]):
    """Run solution"""
    seeds = get_seeds(input_data)
    seed_ranges = parse_seeds(seeds)
    maps = get_maps(input_data)
    key_seeds = get_key_seeds(seed_ranges, maps)
    return find_min_seed_from_key_seeds(key_seeds, maps)


if __name__ == "__main__":
    input_file = Path(__file__).parent.parent / "input.txt"
    input_data = read_input(input_file)
    result = main(input_data)

    output_file = Path(__file__).parent / "result.txt"
    with open(output_file, "w") as fh:
        fh.write(str(result["location"]))
    print(
        f"The lowest seed with loc: {result['location']} is seed: {result['seed']}"
    )
