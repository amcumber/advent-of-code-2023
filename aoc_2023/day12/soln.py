from itertools import zip_longest
from pathlib import Path

import click
from aoc_2023.core import get_input_file, read_file

BROKEN = "#"
WORK = "."
UNKNOWN = "?"


def get_spring_list(line):
    return line.split()[0]


def get_verify_list(line):
    return list(map(int, line.split()[1].split(",")))


def make_test_list(pop_list):
    cur_state = None
    cnt = 0
    test_list = []
    for ele in pop_list:
        if ele != cur_state:
            if cur_state is BROKEN:
                test_list.append(cnt)
            cnt = 1
            cur_state = ele
            continue
        cnt += 1
    if cur_state is BROKEN:
        test_list.append(cnt)
    return test_list


def _verify_list(pop_list, verif_list):
    test_list = make_test_list(pop_list)
    for t, v in zip_longest(test_list, verif_list):
        if t != v:
            return False
    return True


def get_unk_idx(sl):
    indexes = []
    for idx, ele in enumerate(sl):
        if ele != UNKNOWN:
            continue
        indexes.append(idx)
    return indexes


def get_combos(sl, verif_list, unk_idx) -> list[str]:
    sp_list = list(sl)
    combos = []
    if UNKNOWN not in sl and _verify_list(sl, verif_list):
        combos.append(sl)

    else:
        while unk_idx:
            idx = unk_idx.pop(0)
            for added in (BROKEN, WORK):
                first = sp_list
                first[idx] = added
                sp = "".join(first)
                new_combos = get_combos(sp, verif_list, unk_idx)
                for combo in new_combos:
                    if combo not in combos:
                        combos.append(combo)
    return combos


def main_part1(data: list[str]) -> list[int]:
    all_combos = []
    for line in data:
        spring_list = get_spring_list(line)
        verif_list = get_verify_list(line)
        indexes = get_unk_idx(line)
        combos = [combo for combo in get_combos(spring_list, verif_list, indexes)]
        all_combos.append(len(combos))
    return sum(all_combos)


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
