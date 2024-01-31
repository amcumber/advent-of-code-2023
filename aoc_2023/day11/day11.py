from dataclasses import dataclass

TARGET_ID = "#"
DEFAULT_INFILL = "@"
DEFAULT_EMPTY = "."


@dataclass
class Coord:
    """Coordinate class with manhattan distance method"""

    y: int
    x: int

    def __sub__(self, other) -> int:
        Y = self.y - other.y
        X = self.x - other.x
        return Y, X

    def dist(self, other) -> int:
        """Get manhattan distance"""
        d_y, d_x = other - self
        return abs(d_x) + abs(d_y)

    def tup(self) -> tuple[int]:
        """Return the dataclass tuple"""
        return self.y, self.x


def expand_data(
    data: list[str],
    target_id: str = TARGET_ID,
    infill_id: str = DEFAULT_INFILL,
) -> list[str]:
    """Expand data to to represent empty rows/cols have
    appropriate markers"""

    def expand_rows(data):
        new_data = []
        for row in data:
            if is_row_empty(row, target_id):
                new_data.append(infill_id * len(row))
                # continue
            new_data.append(row)
        return new_data

    def expand_cols(data):
        new_data = expand_rows(transpose(data))
        return transpose(new_data)

    new_data = expand_rows(data)
    return expand_cols(new_data)


def transpose(data: list[str]) -> list[str]:
    """Transpose data"""
    return ["".join(col) for col in zip(*data)]


def is_row_empty(row: str, key: str) -> bool:
    """determine if a row is empty"""
    return not row.count(key)


def find_targets(
    data: list[str],
    target_id: str = TARGET_ID,
    infill_id: str = DEFAULT_INFILL,
    infill_val: int = 2,
) -> list[Coord]:
    targets = []
    n_infill = 0
    infill_val -= 1  # correct double count infill
    for y, row in enumerate(data):
        if row.count(infill_id) == len(row):
            n_infill += 1
            continue
        row_infill = get_infill_in_row(row, infill_id)
        y_val = (y - n_infill) + n_infill * infill_val
        targets.extend(
            get_targets_in_row(
                row,
                y_val,
                target_id,
                row_infill=row_infill,
                infill_val=infill_val,
            )
        )
    return targets


def get_targets_in_row(
    row: str,
    y_val: int,
    target_id: str,
    row_infill: list[int],
    infill_val: int,
) -> list[Coord]:
    """Return a list of targets in a row"""
    cnt = row.count(target_id)
    targets = []
    ref_idx = 0
    while cnt:
        x = row.find(target_id, ref_idx)
        n_infill = sum([idx < x for idx in row_infill])
        x_val = (x - n_infill) + n_infill * infill_val

        targets.append(Coord(y_val, x_val))

        ref_idx = x_val + 1
        cnt -= 1
    return targets


def get_infill_in_row(row: str, infill: str | None) -> list[int]:
    """Return a list of infill indices in a row"""
    if infill is None:
        return []
    cnt = row.count(infill)
    infill_idxs = []
    ref_idx = 0
    while cnt:
        x = row.find(infill, ref_idx)
        infill_idxs.append(x)

        ref_idx = x + 1
        cnt -= 1
    return infill_idxs


def get_dists(targets: list[Coord]) -> list[int]:
    dists = []
    while len(targets):
        target = targets.pop(0)
        for other in targets:
            dists.append(target.dist(other))
    return dists


def calc_result(val: list[int]) -> int:
    return sum(val)
