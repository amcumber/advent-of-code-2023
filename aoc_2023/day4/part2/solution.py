import re
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.resolve() / "../../.."))

from aoc_2023.core import read_input


def _parse_line(line: str) -> list[list[int]]:
    winner_str, card_str = line.split(":")[1].split("|")
    return tuple(_parse_str_arr(arr) for arr in (winner_str, card_str))


def _parse_str_arr(array: str) -> list[int]:
    m = re.compile(r"\s+")
    return [int(ele) for ele in m.split(array.strip())]


def parse_input(lines: list[str]) -> tuple[list[int], list[int]]:
    return zip(*[_parse_line(line) for line in lines])


def get_matches(card, winners) -> list[int]:
    return [num for num in card if num in winners]


def score_matches(matches: list[int]) -> int:
    n = len(matches)
    if n > 0:
        return 2 ** (n - 1)
    return 0


def main(input_data: list[str]):
    """Run solution"""
    winning_cards, cards = parse_input(input_data)
    all_matches = [
        get_matches(card, winning_nums)
        for card, winning_nums in zip(cards, winning_cards)
    ]

    return [score_matches(matches) for matches in all_matches]


if __name__ == "__main__":
    input_file = Path(__file__).parent.parent / "input.txt"
    input_data = read_input(input_file)
    result = main(input_data)

    output_file = Path(__file__).parent / "result.txt"
    with open(output_file, "w") as fh:
        fh.write(str(ans := sum(result)))
    print(f"The sum is {ans}")
