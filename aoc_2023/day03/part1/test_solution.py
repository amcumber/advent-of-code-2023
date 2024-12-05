from dataclasses import dataclass

import pytest
from aoc_2023.day03.part1.solution import (
    compare_line,
    main,
    numbers_in_line,
    symbols_in_line,
)


@dataclass
class ProxyMatch:
    _span: tuple[int, int]
    match: str

    def span(self):
        return self._span

    def group(self, int=0):
        return self.match


@pytest.fixture
def example_input():
    return [
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598..",
    ]


@pytest.fixture
def expected_symbol_locs():
    return [
        [],
        [ProxyMatch((3, 4), "")],
        [],
        [ProxyMatch((6, 7), "")],
        [ProxyMatch((3, 4), "")],
        [ProxyMatch((5, 6), "")],
        [],
        [],
        [ProxyMatch((3, 4), ""), ProxyMatch((5, 6), "")],
        [],
    ]


@pytest.fixture
def expected_number_locs():
    return [
        [ProxyMatch((0, 3), "467"), ProxyMatch((5, 8), "114")],
        [],
        [ProxyMatch((2, 4), "35"), ProxyMatch((6, 9), "633")],
        [],
        [ProxyMatch((0, 3), "617")],
        [ProxyMatch((7, 9), "58")],
        [ProxyMatch((2, 5), "592")],
        [ProxyMatch((6, 9), "755")],
        [],
        [ProxyMatch((1, 4), "664"), ProxyMatch((5, 8), "598")],
    ]


def example_line_1():
    return "617*......"


def expected_sym_1():
    return [ProxyMatch((3, 4), "")]


def expected_num_1():
    return [ProxyMatch((0, 3), "617")]


def expected_compare_1():
    return [617]


def example_line_2():
    return "617*551+.."


def expected_sym_2():
    return [ProxyMatch((3, 4), ""), ProxyMatch((7, 8), "")]


def expected_num_2():
    return [ProxyMatch((0, 3), "617"), ProxyMatch((4, 7), "551")]


def expected_compare_2():
    return [617, 551]


def example_line_3():
    return ".........."


def expected_sym_3():
    return []


def expected_num_3():
    return []


def expected_compare_3():
    return []


def example_line_4():
    return "+$%......."


def expected_sym_4():
    return [
        ProxyMatch((0, 1), ""),
        ProxyMatch((1, 2), ""),
        ProxyMatch((2, 3), ""),
    ]


@pytest.mark.parametrize(
    ["line", "expected"],
    [
        (example_line_1(), expected_sym_1()),
        (example_line_2(), expected_sym_2()),
        (example_line_3(), expected_sym_3()),
        (example_line_4(), expected_sym_4()),
    ],
)
def test_symbols_in_line(line, expected):
    result = symbols_in_line(line)
    assert len(result) == len(expected), "Failed expected len"
    for r_mat, e_mat in zip(result, expected):
        assert r_mat.span() == e_mat.span(), "Failed Span"


@pytest.mark.parametrize(
    ["line", "expected"],
    [
        (example_line_1(), expected_num_1()),
        (example_line_2(), expected_num_2()),
        (example_line_3(), expected_num_3()),
    ],
)
def test_numbers_in_line(line, expected):
    result = numbers_in_line(line)
    assert len(result) == len(expected), "Failed expected len"
    for r_mat, e_mat in zip(result, expected):
        assert r_mat.span() == e_mat.span(), "Failed Span"
        assert r_mat.group() == e_mat.group(), "Failed Span"


def test_numbers_in_example(example_input, expected_number_locs):
    result = [numbers_in_line(line) for line in example_input]
    assert len(result) == len(expected_number_locs), "Failed expected len"
    for r_line, e_line in zip(result, expected_number_locs):
        assert len(r_line) == len(e_line), "Failed expected line len"
        for r_mat, e_mat in zip(r_line, e_line):
            assert r_mat.span() == e_mat.span(), "Failed Span"
            assert r_mat.group() == e_mat.group(), "Failed Span"


def test_symbols_in_example(example_input, expected_symbol_locs):
    result = [symbols_in_line(line) for line in example_input]
    assert len(result) == len(expected_symbol_locs), "Failed expected len"
    for r_line, e_line in zip(result, expected_symbol_locs):
        assert len(r_line) == len(e_line), "Failed expected line len"
        for r_mat, e_mat in zip(r_line, e_line):
            assert r_mat.span() == e_mat.span(), "Failed Span"


@pytest.mark.parametrize(
    ["sym", "num", "expected"],
    [
        (expected_sym_1(), expected_num_1(), expected_compare_1()),
        (expected_sym_2(), expected_num_2(), expected_compare_2()),
        (expected_sym_3(), expected_num_3(), expected_compare_3()),
    ],
)
def test_compare_line(sym, num, expected):
    result = compare_line(sym, num)
    for r_num, e_num in zip(result, expected):
        assert r_num == e_num, "failed compare"


def test_main(example_input):
    expected_sum = 4361
    result = main(example_input)
    assert sum(result) == expected_sum, "Failed main"
