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
    left, right = map(
        list, zip(*(map(int, line.split()) for line in text.splitlines()))
    )
    left.sort()
    right.sort()
    return sum(abs(l - r) for l, r in zip(left, right))


print(f"sample a: {solve_a(samp)}")
print(f"answer a: {solve_a(data)}\n")


def solve_b(text):
    left, right = zip(*(map(int, line.split()) for line in text.splitlines()))
    lc = Counter(left)
    rc = Counter(right)
    return sum(num * lc[num] * rc[num] for num in lc)


print(f"sample b: {solve_b(samp)}")
print(f"answer b: {solve_b(data)}")
