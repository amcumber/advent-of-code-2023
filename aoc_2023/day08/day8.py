"""tools for day 8"""
DIR2NUM = {id_: idx for idx, id_ in enumerate("LR")}


def parse_directions(
    input_data: list[str], dir_key: dict[str, int] = DIR2NUM
) -> tuple[int, ...]:
    dir_str = input_data[0]
    return tuple(dir_key[dir_] for dir_ in dir_str)


def parse_map(input_data: list[str]) -> dict[str, tuple[str, str]]:
    def _clean_dirty_vals(vals):
        return [val.strip() for val in vals.strip("()").split(",")]

    new_map = {}
    for line in input_data[2:]:
        key, vals_dirty = (ele.strip() for ele in line.split("="))
        new_map[key] = tuple(_clean_dirty_vals(vals_dirty))
    return new_map
