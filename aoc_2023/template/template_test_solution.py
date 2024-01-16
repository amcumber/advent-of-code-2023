import sys
from pathlib import Path

import pytest

if __name__ == "__main__":
    sys.path.append(str(Path(__file__).parent.resolve() / "../../.."))

from aoc_2023.xxx import main


def example_input():
    return [
        "",
    ]


def expected_result():
    return 0


@pytest.mark.parametrize(
    ["input_data", "expected"],
    [
        (example_input(), expected_result()),
    ],
)
def test_main(input_data, expected):
    result = main(input_data)
    assert result == expected
