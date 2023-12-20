from pathlib import Path


def read_input(file: Path) -> list[int]:
    """Read input.txt and parse each line with a first / last number
    described in rules"""
    with open(file, "r") as fh:
        codes = []
        for line in fh.readlines():
            numbers = [e for e in line if e.isnumeric()]
            num_str = f"{numbers[0]}{numbers[-1]}"
            codes.append(int(num_str))
        return codes


def main():
    """Run solution"""
    input_file = Path(__file__).parent.parent / "input.txt"
    output_file = Path(__file__).parent / "result.txt"
    codes = read_input(input_file)
    result = sum(codes)
    with open(output_file, "w") as fh:
        fh.write(str(result))
    print(result)


if __name__ == "__main__":
    main()
