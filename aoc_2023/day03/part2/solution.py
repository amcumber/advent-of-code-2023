import re
from functools import reduce
from pathlib import Path


def read_input(file: Path) -> list[str]:
    """Read input.txt and return a list of stripped strings"""
    with open(file, "r") as fh:
        return [line.strip() for line in fh.readlines()]


def symbols_in_line(line: str) -> tuple[re.Match]:
    """Get the symbol indices in a line that are not . or digit"""
    pattern = re.compile(r"[*]")
    return _get_all_matches(line, pattern)


def numbers_in_line(line: str) -> list[re.Match]:
    """Get the symbol indices in a line that are not . or digit"""
    pattern = re.compile(r"\d+")
    return _get_all_matches(line, pattern)


def _get_all_matches(line: str, pattern: re.Pattern) -> list[re.Match]:
    idx = 0
    symbols = []
    while matched := pattern.search(line, idx):
        symbols.append(matched)
        idx = matched.span()[1]
    return symbols


def match_numbers_to_symbols(
    symbols: list[list[re.Match]], numbers: list[list[re.Match]]
) -> list[list[int]]:
    """Find matching numbers that are adjacent to valid symbols and append them
    to a nested list"""
    matches = []
    prev_n_line = []
    s_line = []
    n_line = []
    for next_s_line, next_n_line in zip(symbols, numbers):
        matches.extend(
            compare_lines(
                s_line,
                [
                    prev_n_line,
                    n_line,
                    next_n_line,
                ],
            )
        )

        prev_n_line = n_line
        s_line = next_s_line
        n_line = next_n_line

    # Last line
    matches.extend(compare_lines(s_line, [prev_n_line, n_line]))

    return matches


def compare_lines(s_line: list[re.Match], n_lines: list[list[re.Match]]) -> list[int]:
    matches = []
    for sym in s_line:
        adj_sym = []
        for n_line in n_lines:
            adj_sym.extend(compare_sym(sym, n_line))
        matches.append(adj_sym)
    return matches


def compare_sym(sym: re.Match, n_line: list[re.Match]) -> list[int]:
    """Compare a symbol line and a number line to determine if any numbers are
    adjacent"""
    matches = []
    sym_idx, _ = sym.span()

    for num in n_line:
        num_start, num_end = num.span()

        if num_start - 1 <= sym_idx and num_end >= sym_idx:
            matches.append(int(num.group()))
    return matches


def prod_match_sets(match_set: list[int]) -> int:
    """Calculate the product of a match set, returning 0 if list len is 0 or 1"""
    if len(match_set) < 2:
        return 0
    return reduce(lambda x, y: x * y, match_set)


def main(input_data: list[str]):
    """Run solution"""

    symbols = [symbols_in_line(line) for line in input_data]
    numbers = [numbers_in_line(line) for line in input_data]
    matches = match_numbers_to_symbols(symbols, numbers)
    return [prod_match_sets(match_set) for match_set in matches]


if __name__ == "__main__":
    input_file = Path(__file__).parent.parent / "input.txt"
    input_data = read_input(input_file)
    result = main(input_data)

    output_file = Path(__file__).parent / "result.txt"
    with open(output_file, "w") as fh:
        fh.write(str(ans := sum(result)))
    print(f"The sum is {ans}")
