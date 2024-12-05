"""Prototype for part 2 day 5"""

from typing import Iterable

import matplotlib.pyplot as plt

if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.append(str(Path(__file__).parent.resolve() / "../../.."))

from aoc_2023.day05.day5 import SparseMap, get_maps, get_seeds
from aoc_2023.day05.part2.solution_d5p2 import get_paths, parse_seeds


def input_tbr():
    return [
        "seeds: 79 14 55 13",
        "",
        "seed-to-soil map:",
        "50 98 2",
        "52 50 48",
        "",
        "soil-to-fertilizer map:",
        "0 15 37",
        "37 52 2",
        "39 0 15",
        "",
        "fertilizer-to-water map:",
        "49 53 8",
        "0 11 42",
        "42 0 7",
        "57 7 4",
        "",
        "water-to-light map:",
        "88 18 7",
        "18 25 70",
        "",
        "light-to-temperature map:",
        "45 77 23",
        "81 45 19",
        "68 64 13",
        "",
        "temperature-to-humidity map:",
        "0 69 1",
        "1 0 69",
        "",
        "humidity-to-location map:",
        "60 56 37",
        "56 93 4",
    ]


def visualize(
    seed_ranges: list[Iterable[int]], maps: dict[str, SparseMap]
) -> tuple[plt.Figure, plt.Axes]:
    """Visualize"""
    x = []
    y = []
    for s_range in seed_ranges:
        paths = get_paths(s_range, maps)
        x.extend(list(paths.keys()))
        y.extend([path[-1] for path in paths.values()])
    fig, ax = plt.subplots(1, 1)
    ax.plot(x, y, "k+")
    return fig, ax


def main(input_data: list[str]) -> tuple[plt.Figure, plt.Axes]:
    """prototype"""
    seeds = get_seeds(input_data)
    seed_ranges = parse_seeds(seeds)
    maps = get_maps(input_data)
    fig, ax = visualize(seed_ranges, maps)
    return fig, ax


if __name__ == "__main__":
    fig, ax = main(input_tbr())
    plt.show()
