import sys
from dataclasses import dataclass
from pathlib import Path

import click
from aoc_2023.core import get_input_file, read_file


def main_part1(data: list[str]) -> list[int]:
    return None


def main_part2(data: list[str]) -> list[int]:
    return None


def calc_result(val: list[int]) -> int:
    return sum(val)


@click.group(help="AOC 2023 day 12 solution")
def cli():
    """Command Line Interface for day12"""


@cli.command(help="part1 solution")
@click.option("--file", default=get_input_file(__file__))
def part1(file):
    data = read_file(Path(file))
    print(main_part1(data))


@cli.command(help="part2 solution")
@click.option("--file", default=get_input_file(__file__))
def part2(file):
    data = read_file(Path(file))
    print(main_part2(data))
