import re
from pathlib import Path


def read_input(file: Path) -> list[str]:
    """Read input.txt and return a list of stripped strings"""
    with open(file, "r") as fh:
        return [line.strip() for line in fh.readlines()]


def symbols_in_line(line: str) -> tuple[int]:
    """Get the symbol indices in a line that are not . or \d"""
    pattern = re.compile(r"[*]")
    return _get_all_matches(line, pattern)


def numbers_in_line(line: str) -> list[re.Match]:
    """Get the symbol indices in a line that are not . or \d"""
    pattern = re.compile(r"[\d]+")
    return _get_all_matches(line, pattern)


def _get_all_matches(line: str, pattern: re.Pattern) -> list[re.Match]:
    idx = 0
    symbols = []
    while matched := pattern.search(line, idx):
        symbols.append(matched)
        idx = matched.span()[1]
    return symbols


def find_matching_numbers(
    symbols: list[tuple[int]], numbers: list[tuple[int, int]]
) -> list[tuple[int, int]]:
    """Find matching numbers that are adjacent to valid symbols and append them
    to a list"""
    # FIXME: need to restructure comparison to multiply matches
    matches = []
    prev_s_line = []
    prev_n_line = []
    for s_line, n_line in zip(symbols, numbers):
        matches.extend(compare_line(s_line, prev_n_line))
        matches.extend(compare_line(s_line, n_line))
        matches.extend(compare_line(prev_s_line, n_line))
        prev_s_line = s_line
        prev_n_line = n_line
    return matches


def compare_line(s_line: list[int], n_line: list[re.Match]) -> list[int]:
    """Compare a symbol line and a number line to determine if any numbers are
    adjacent"""
    matches = []
    for num in n_line:
        num_start, num_end = num.span()
        for sym in s_line:
            sym_idx, _ = sym.span()
            if num_start - 1 <= sym_idx and num_end >= sym_idx:
                matches.append(int(num.group()))
    return matches


def main(input_data: list[str]):
    """Run solution"""

    symbols = [symbols_in_line(line) for line in input_data]
    numbers = [numbers_in_line(line) for line in input_data]
    return find_matching_numbers(symbols, numbers)


if __name__ == "__main__":
    input_file = Path(__file__).parent.parent / "input.txt"
    input_data = read_input(input_file)
    result = main(input_data)

    output_file = Path(__file__).parent / "result.txt"
    with open(output_file, "w") as fh:
        fh.write(str(ans := sum(result)))
    print(f"The sum is {ans}")
