from pathlib import Path

str2num = {
    "one": "1",
    "two": "2",
    "six": "6",
    "four": "4",
    "five": "5",
    "nine": "9",
    "zero": "0",
    "three": "3",
    "seven": "7",
    "eight": "8",
}


def read_input_with_string(file: Path) -> list[int]:
    """Read input.txt and parse each line with a first / last number
    described in rules"""
    with open(file, "r") as fh:
        codes = []
        for line in fh.readlines():
            line = clean_line(line)
            numbers = [e for e in line if e.isnumeric()]
            num_str = f"{numbers[0]}{numbers[-1]}"
            codes.append(int(num_str))
        return codes


def clean_line(line: str):
    """Convert a string with number words to ints"""
    for key, val in str2num.items():
        line = line.replace(key, f"{key}{val}{key}")
        # The trick is that numbers were concatenated like eightwo
        # - this keeps order and generates both 8 and 2
    return line


def main():
    """Run solution"""
    input_file = Path(__file__).parent.parent / "input.txt"
    output_file = Path(__file__).parent / "result.txt"
    codes = read_input_with_string(input_file)
    result = sum(codes)
    with open(output_file, "w") as fh:
        fh.write(str(result))
    print(result)


if __name__ == "__main__":
    main()
