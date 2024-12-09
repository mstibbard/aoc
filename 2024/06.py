import numpy as np
from aocd import get_data
from dotenv import load_dotenv

load_dotenv()
data = get_data(day=6, year=2024).splitlines()
samp = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...""".splitlines()

DIRECTIONS = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
TURN_RIGHT = {"^": ">", ">": "v", "v": "<", "<": "^"}


def solve_a(area):
    ma = np.array([list(line) for line in area])

    g = np.where(ma == "^")
    pos = (g[0][0], g[1][0])
    d = "^"

    visited = []
    while True:
        visited.append(pos)
        next_pos = (pos[0] + DIRECTIONS[d][0], pos[1] + DIRECTIONS[d][1])
        if 0 <= next_pos[0] < ma.shape[0] and 0 <= next_pos[1] < ma.shape[1]:
            if ma[next_pos] == "#":
                d = TURN_RIGHT[d]
            else:
                ma[pos[0]][pos[1]] = "X"  # for visual debugging
                ma[next_pos[0]][next_pos[1]] = d  # for visual debugging
                pos = next_pos
        else:
            break
    # print(ma)

    return len(set(visited))


print(f"sample a: {solve_a(samp)}")
print(f"answer a: {solve_a(data)}\n")


def solve_b(area):
    return 0


print(f"sample b: {solve_b(samp)}")
print(f"answer b: {solve_b(data)}")
