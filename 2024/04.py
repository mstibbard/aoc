import re
from aocd import get_data
from dotenv import load_dotenv
from typing import Dict, List, Optional, Pattern, Tuple, TypedDict

load_dotenv()
data = get_data(day=4, year=2024).splitlines()
samp = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""".splitlines()


class Match(TypedDict):
    dir: str
    string: str
    start_pos: Tuple[int, int]
    found: str
    found_at: int
    A_at: Optional[Tuple[int, int]]


def get_vertical(grid: List[str]) -> List[str]:
    """Returns the grid as a list of vertical strings. Essentially rotating the grid."""
    return ["".join(row[i] for row in grid) for i in range(len(grid[0]))]


def get_diagonal(grid: List[str], row: int, col: int, right: bool) -> str:
    """Returns the diagonal string in the grid starting from the given row and column."""
    chars = []
    while row < len(grid) and 0 <= col < len(grid[0]):
        chars.append(grid[row][col])
        row += 1
        col += 1 if right else -1
    return "".join(chars)


def find_matches(
    string: str, pos: Tuple[int, int], label: str, pattern: Pattern
) -> List[Match]:
    """Finds all matches of the given pattern in the given string."""
    matches = []
    for match in re.finditer(pattern, string):
        matches.append(
            {
                "dir": label,
                "string": string,
                "start_pos": pos,
                "found": match.group(),
                "found_at": match.start(),
            }
        )
    return matches


def solve_a(grid):
    matches = []
    grid_height = len(grid)
    grid_width = len(grid[0])
    pattern = re.compile(r"XMAS")
    pattern_rev = re.compile(r"SAMX")

    for row, line in enumerate(grid):
        matches.extend(find_matches(line, (row, 0), "HOR", pattern))
        matches.extend(find_matches(line, (row, 0), "HOR", pattern_rev))

    for col, line in enumerate(get_vertical(grid)):
        matches.extend(find_matches(line, (0, col), "VER", pattern))
        matches.extend(find_matches(line, (0, col), "VER", pattern_rev))

    for col in range(grid_width):
        dr = get_diagonal(grid, 0, col, right=True)
        matches.extend(find_matches(dr, (0, col), "DR", pattern))
        matches.extend(find_matches(dr, (0, col), "DR", pattern_rev))

        dl = get_diagonal(grid, 0, col, right=False)
        matches.extend(find_matches(dl, (0, col), "DL", pattern))
        matches.extend(find_matches(dl, (0, col), "DL", pattern_rev))

    for row in range(1, grid_height):
        dr = get_diagonal(grid, row, 0, right=True)
        matches.extend(find_matches(dr, (row, 0), "DR", pattern))
        matches.extend(find_matches(dr, (row, 0), "DR", pattern_rev))

        dl = get_diagonal(grid, row, grid_width - 1, right=False)
        matches.extend(find_matches(dl, (row, grid_width - 1), "DL", pattern))
        matches.extend(find_matches(dl, (row, grid_width - 1), "DL", pattern_rev))

    # print(matches)
    return len(matches)


print(f"sample a: {solve_a(samp)}")
print(f"answer a: {solve_a(data)}\n")


def find_overlapping_matches(matches: List[Match]) -> Dict[Tuple[int, int], int]:
    """Finds all occurrences where two 'A' positions overlap."""
    for i, o in enumerate(matches):
        if o["dir"] == "DR":
            matches[i]["A_at"] = (
                o["start_pos"][0] + o["found_at"] + 1,
                o["start_pos"][1] + o["found_at"] + 1,
            )
        if o["dir"] == "DL":
            matches[i]["A_at"] = (
                o["start_pos"][0] + o["found_at"] + 1,
                o["start_pos"][1] - o["found_at"] - 1,
            )

    matches_count = {}
    for o in matches:
        key = o["A_at"]
        count = 1
        if key in matches_count:
            count = matches_count[key] + 1
        matches_count[key] = count

    return {key: value for key, value in matches_count.items() if value == 2}


def solve_b(grid):
    matches = []
    grid_height = len(grid)
    grid_width = len(grid[0])
    pattern = re.compile(r"MAS")
    pattern_rev = re.compile(r"SAM")

    for col in range(grid_width):
        dr = get_diagonal(grid, 0, col, right=True)
        matches.extend(find_matches(dr, (0, col), "DR", pattern))
        matches.extend(find_matches(dr, (0, col), "DR", pattern_rev))

        dl = get_diagonal(grid, 0, col, right=False)
        matches.extend(find_matches(dl, (0, col), "DL", pattern))
        matches.extend(find_matches(dl, (0, col), "DL", pattern_rev))

    for row in range(1, grid_height):
        dr = get_diagonal(grid, row, 0, right=True)
        matches.extend(find_matches(dr, (row, 0), "DR", pattern))
        matches.extend(find_matches(dr, (row, 0), "DR", pattern_rev))

        dl = get_diagonal(grid, row, grid_width - 1, right=False)
        matches.extend(find_matches(dl, (row, grid_width - 1), "DL", pattern))
        matches.extend(find_matches(dl, (row, grid_width - 1), "DL", pattern_rev))

    overlap = find_overlapping_matches(matches)
    # print(matches)
    # print(overlap)
    return len(overlap)


print(f"sample b: {solve_b(samp)}")
print(f"answer b: {solve_b(data)}")
