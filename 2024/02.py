from aocd import get_data
from dotenv import load_dotenv

load_dotenv()
data = get_data(day=2, year=2024)
samp = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""


def validate_levels(levels):
    diffs = [
        (abs(b - a), "pos" if b - a > 0 else "neg") for a, b in zip(levels, levels[1:])
    ]
    grad_dec = all(1 <= o[0] <= 3 and o[1] == "neg" for o in diffs)
    grad_inc = all(1 <= o[0] <= 3 and o[1] == "pos" for o in diffs)
    return grad_dec or grad_inc


def solve_a(text):
    count = 0
    for o in text.splitlines():
        levels = [int(p) for p in o.split()]
        if validate_levels(levels):
            count += 1
    return count


print(f"sample a: {solve_a(samp)}")
print(f"answer a: {solve_a(data)}\n")


def solve_b(text):
    count = 0
    for o in text.splitlines():
        levels = [int(p) for p in o.split()]
        orig_safe = validate_levels(levels)

        # Create all possible alternate sequences without a digit
        alt_seq = [levels[:i] + levels[i + 1 :] for i in range(len(levels))]
        any_alt_safe = any(validate_levels(p) for p in alt_seq)
        if orig_safe or any_alt_safe:
            count += 1
    return count


print(f"sample b: {solve_b(samp)}")
print(f"answer b: {solve_b(data)}")
