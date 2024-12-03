import re
from aocd import get_data
from dotenv import load_dotenv

load_dotenv()
data = get_data(day=3, year=2024)
samp = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"


def solve_a(text):
    sum = 0
    for match in re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)", text):
        x, y = map(int, match.groups())
        sum += x * y
    return sum


print(f"sample a: {solve_a(samp)}")
print(f"answer a: {solve_a(data)}\n")

samp2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


pattern = r"mul\((?P<x>\d{1,3}),(?P<y>\d{1,3})\)|(?P<do>do\(\))|(?P<dont>don\'t\(\))"


def solve_b(text):
    enabled = True
    sum = 0
    for match in re.finditer(pattern, text):
        if match.group("dont"):
            enabled = False
        elif match.group("do"):
            enabled = True
        elif enabled:
            sum += int(match.group("x")) * int(match.group("y"))
    return sum


print(f"sample b: {solve_b(samp2)}")
print(f"answer b: {solve_b(data)}")
