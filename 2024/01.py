from aocd import get_data
from collections import Counter
from dotenv import load_dotenv

load_dotenv()
data = get_data(day=1, year=2024)
samp = """3   4
4   3
2   5
1   3
3   9
3   3"""


def solve_a(text):
    lines = text.splitlines()
    left = []
    right = []
    for line in lines:
        l, r = line.split()
        left.append(int(l))
        right.append(int(r))
    left.sort()
    right.sort()
    combined = []
    for i, v in enumerate(left):
        combined.append({"left": v, "right": right[i], "distance": abs(v - right[i])})
    return sum(o["distance"] for o in combined)


print(f"sample a: {solve_a(samp)}")
print(f"answer a: {solve_a(data)}\n")


def solve_b(text):
    lines = text.splitlines()
    left = []
    right = []
    for line in lines:
        l, r = line.split()
        left.append(int(l))
        right.append(int(r))
    lc = Counter(left)
    rc = Counter(right)
    sum_distance = 0
    for o in lc:
        l = lc[o]
        r = rc[o]
        for i in range(l):
            sum_distance += o * r
    return sum_distance


print(f"sample b: {solve_b(samp)}")
print(f"answer b: {solve_b(data)}")
