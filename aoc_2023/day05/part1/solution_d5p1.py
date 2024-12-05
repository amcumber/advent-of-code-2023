"""Solution to part 1 day 5"""

if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.append(str(Path(__file__).parent.resolve() / "../../.."))

from aoc_2023.core import read_input
from aoc_2023.day05.day5 import get_maps, get_seeds, walk_almanac, SparseMap

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


def get_paths(
    seeds: list[int], maps: dict[str, SparseMap]
) -> dict[int, dict[str, int]]:
    paths = {}
    for seed in seeds:
        path, _ = walk_almanac(ALMANAC, seed, maps, start_name=START_NAME)
        paths[seed] = path

    return paths


def find_min_loc(paths: dict[int, list[int]]) -> tuple[int, int]:
    loc2seed = {}
    for seed, path in paths.items():
        loc2seed[path[-1]] = seed
    min_loc = min(loc2seed.keys())
    return min_loc, loc2seed[min_loc]


def main(input_data: list[str]):
    """Run solution"""
    seeds = get_seeds(input_data)
    maps = get_maps(input_data)
    paths = get_paths(seeds, maps)
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
