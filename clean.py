from pathlib import Path


class CleanValueError(Exception):
    """Value Error"""


NEW_DIR = Path(__file__).parent / "usr"
OLD_DIR = Path(__file__).parent / "aoc_2023"


def minus_root(root: Path, path: Path) -> Path:
    if not all([part in path.parts for part in root.parts]):
        raise CleanValueError("Not part of path")

    rel_path = list(path.parts)
    for part in root.parts:
        if 0 != rel_path.index(part):
            raise CleanValueError("Incorrect index, aborting")
        rel_path.pop(0)
    new_path = Path()
    for part in rel_path:
        new_path /= part
    return new_path


def get_new_root(path: Path, old_root: Path, new_root: Path) -> Path:
    rel_file = minus_root(old_root, path)
    return new_root / rel_file


def replace_file(file: Path, old_root: Path, new_root: Path) -> Path:
    new_file = get_new_root(file, old_root, new_root)
    new_file.parent.mkdir(exist_ok=True, parents=True)
    file.rename(new_file)


def main(old_root: Path, new_root: Path, file_pattern: str = "*.txt") -> None:
    for file in old_root.rglob(file_pattern):
        replace_file(file, old_root, new_root)


if __name__ == "__main__":
    main(OLD_DIR, NEW_DIR)
