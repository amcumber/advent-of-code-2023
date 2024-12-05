"""Solution to day 7 part 1
"""

import sys
from pathlib import Path

if __name__ == "__main__":
    sys.path.append(str(Path(__file__).parent.resolve() / "../../.."))

from aoc_2023.core import parse_line, read_input
from aoc_2023.day07.day7 import CamelHand, calc_result, rank_hands, sort_wagers

CARD_RANK_7P1 = {
    card: rank for rank, card in enumerate(reversed("AKQJT98765432"))
}


def parse_camel_line_7p1(
    line: str, card_rank: dict[str, int]
) -> tuple[CamelHand, int]:
    """Parse camel cards hand into the hand and wager"""
    hand = parse_line(line, divider=" ", idx=0)
    wager = parse_line(line, divider=" ", idx=1)

    return CamelHand(hand, card_rank=card_rank), int(wager)


def main(input_data: list[str]) -> list[int]:
    """Main for day7 part 1 - camel cards"""
    hands, wagers = list(
        zip(
            *[parse_camel_line_7p1(line, CARD_RANK_7P1) for line in input_data]
        )
    )
    ranks = rank_hands(hands)
    return sort_wagers(ranks, wagers)


if __name__ == "__main__":
    input_file = Path(__file__).parent.parent / "input.txt"
    input_data = read_input(input_file)
    result = main(input_data)
    val = calc_result(result)

    output_file = Path(__file__).parent / "result.txt"
    with open(output_file, "w") as fh:
        fh.write(str(val))
    print(f"The results: {val}")
