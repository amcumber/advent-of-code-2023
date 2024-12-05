from pathlib import Path

Draw = dict[str, int]
Game = dict[int, list[Draw]]


def parse_input(file: Path) -> list[Game]:
    """Read input.txt and parse each line with a first / last number
    described in rules"""
    with open(file, "r") as fh:
        return [parse_line(line) for line in fh.readlines()]


def parse_line(line: str) -> Game:
    """Convert a string line to a nested dict of games and sets"""
    game_str, sets = line.split(":")
    game_no = int(game_str.strip("Game "))
    set_results = parse_sets(sets)
    return {game_no: set_results}


def parse_sets(sets: str) -> list[Draw]:
    """Parse a stringy set (e.g. 4 red, 7 blue; 10 red, 11 green)"""
    return [parse_draw(draw) for draw in sets.split(";")]


def parse_draw(draw: str) -> Draw:
    """Parse a stringy draw (e.g. '1 green, 1 blue, 12 red')"""
    parsed_draw = {}
    for ele in draw.split(","):
        num, key = ele.strip().split(" ")
        parsed_draw[key.strip().lower()] = int(num)
    return parsed_draw


def get_game_maxes(game: Game) -> dict[str, int]:
    """Get the maxes from a game"""
    game_id = list(game_ids := game.keys()).pop()
    assert len(game_ids) == 1, "Only can process 1 game at a time"
    game_maxes = {}
    for draw in game[game_id]:
        for color, n_cube in draw.items():
            if n_cube > game_maxes.get(color, 0):
                game_maxes[color] = n_cube
    return game_maxes


def evaluate_game(game: Game, rules: dict[str, int]) -> bool:
    """Evaluate a game's maxes and the rules"""
    game_maxes = get_game_maxes(game)
    for color, obs_cubes in game_maxes.items():
        rule_cubes = rules.get(color, 0)
        if rule_cubes < obs_cubes:
            return False
    return True


def evaluate_games(games: list[Game], rules: dict[str, int]) -> list[int]:
    return [
        list(game.keys()).pop() for game in games if evaluate_game(game, rules)
    ]


def power_set_game(game: Game):
    power_set = 1
    for val in game.values():
        power_set *= val
    return power_set


def main():
    """Run solution"""
    input_file = Path(__file__).parent.parent / "input.txt"
    output_file = Path(__file__).parent / "result.txt"
    games = parse_input(input_file)
    game_maxes = [get_game_maxes(game) for game in games]
    result = [power_set_game(game) for game in game_maxes]
    with open(output_file, "w") as fh:
        fh.write(str(ans := sum(result)))
    print(f"The sum is {ans}")


if __name__ == "__main__":
    main()
