from pathlib import Path

import click
from aoc_2023.core import get_input_file, read_file

GAL = "#"


def find_gals(data):
    gals = []
    for row, line in enumerate(data):
        for col, ele in enumerate(line):
            if ele == GAL:
                gals.append((row, col))
    return gals


def find_wormholes(gals):
    gal_rows, gal_cols = [ele for ele in zip(*gals)]
    min_row = min(gal_rows)
    max_row = max(gal_rows)

    min_col = min(gal_cols)
    max_col = max(gal_cols)

    wh_rows = []
    wh_cols = []
    for row in range(min_row, max_row):
        if row not in gal_rows:
            wh_rows.append(row)

    for col in range(min_col, max_col):
        if col not in gal_cols:
            wh_cols.append(col)
    return [wh_rows, wh_cols]


def get_dist(first_gal, second_gal, worm_holes, dist_val):
    dist = 0
    x1, y1 = first_gal
    x2, y2 = second_gal
    min_x, max_x = (fun(x1, x2) for fun in (min, max))
    min_y, max_y = (fun(y1, y2) for fun in (min, max))
    span_x = range(min_x, max_x)
    span_y = range(min_y, max_y)
    dist = abs(max_x - min_x) + abs(max_y - min_y)
    wh_row, wh_col = worm_holes
    for wh_x in wh_row:
        if wh_x in span_x:
            dist += dist_val - 1
    for wh_y in wh_col:
        if wh_y in span_y:
            dist += dist_val - 1
    return dist


def find_distances(
    first_gal: tuple[int, int],
    gals: list[tuple[int, int]],
    worm_holes: list[int],
    dist_val: int,
) -> tuple[tuple[int, int], int]:
    dist = 0
    for second_gal in gals:
        dist += get_dist(first_gal, second_gal, worm_holes, dist_val)
    return dist


def match_gals(gals, worm_holes, dist_val):
    matches = []
    gals_copy = gals.copy()
    for gal in gals:
        gals_copy.pop(0)
        dists = find_distances(gal, gals_copy, worm_holes, dist_val)
        if not dists:
            continue
        matches.append(dists)
    return matches


def main_part1(data):
    gals = find_gals(data)
    worm_holes = find_wormholes(gals)
    result = match_gals(gals, worm_holes, 2)
    return sum(result)


def main_part2(data, dist_val):
    gals = find_gals(data)
    worm_holes = find_wormholes(gals)
    result = match_gals(gals, worm_holes, dist_val)
    return sum(result)


@click.group(help="AOC 2023 day 11 solution")
def cli():
    """Command Line Interface for day11"""


@cli.command(help="part1 solution")
@click.option("--file", default=get_input_file(__file__))
def part1(file):
    data = read_file(Path(file))
    print(main_part1(data))


@cli.command(help="part2 solution")
@click.option("--file", default=get_input_file(__file__))
def part2(file):
    data = read_file(Path(file))
    age = 1_000_000
    print(main_part2(data, age))
