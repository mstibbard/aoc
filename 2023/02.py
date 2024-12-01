from aocd import get_data
from dotenv import load_dotenv

load_dotenv()
data = get_data(day=2, year=2023)
sample = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

MAX_CUBES = {"red": 12, "green": 13, "blue": 14}


def process_game(text: str) -> int:
    id, game = text.split(sep=": ")
    id = int(id.removeprefix("Game "))
    hands = game.split(sep="; ")
    possible = True
    for hand in hands:
        colours = {"red": 0, "green": 0, "blue": 0}
        cubes = hand.split(sep=", ")
        for cube in cubes:
            num, colour = cube.split()
            colours[colour] = int(num)
        if any(colours[colour] > MAX_CUBES[colour] for colour in colours):
            possible = False
    return id if possible else 0


def solve_a(text: str) -> int:
    return sum(process_game(line) for line in text.splitlines())


print(f"sample a: {solve_a(sample)}")
print(f"solution a: {solve_a(data)}\n")


def calculate_powers(text):
    id, game = text.split(sep=": ")
    hands = game.split(sep="; ")
    min_cubes = {"red": 0, "green": 0, "blue": 0}
    for hand in hands:
        cubes = hand.split(sep=", ")
        for cube in cubes:
            num, colour = cube.split()
            min_cubes[colour] = max(min_cubes[colour], int(num))
    return min_cubes["red"] * min_cubes["green"] * min_cubes["blue"]


def solve_b(text: str) -> int:
    return sum(calculate_powers(line) for line in text.splitlines())


print(f"sample b: {solve_b(sample)}")
print(f"solution b: {solve_b(data)}")
