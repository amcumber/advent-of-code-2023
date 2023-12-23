import sys
from pathlib import Path

import pytest

sys.path.append(str(Path(__file__).parent.resolve() / "../../.."))

from aoc_2023.day5.part1.solution import main
from aoc_2023.day5.test_day5 import example_input


def test_main(example_input):
    result, *_ = main(example_input)
    expected = 35
    assert expected == result
