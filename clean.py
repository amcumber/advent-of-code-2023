from pathlib import Path

NEW_DIR = Path(__file__).parent / "usr"
OLD_DIR = Path(__file__).parent / "aoc_2023"

from aoc_2023.core import replace_file


def main(old_root: Path, new_root: Path, file_pattern: str = "*.txt") -> None:
    for file in old_root.rglob(file_pattern):
        replace_file(file, old_root, new_root)


if __name__ == "__main__":
    main(OLD_DIR, NEW_DIR)
