from aocd import get_data
from dotenv import load_dotenv

load_dotenv()
data = get_data(day=1, year=2023)
sample_a = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""


def get_digits(text: str) -> int:
    first = True
    for c in text:
        if c.isdigit():
            if first:
                f = c
            l = c
            first = False
    return int(f + l)


def solve_a(text: str) -> int:
    lines = text.splitlines()
    result = 0
    for line in lines:
        result += get_digits(line)
    return result


print(f"sample a: {solve_a(sample_a)}")
print(f"solution a: {solve_a(data)}\n")

sample_b = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

NUM_DICT = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def convert_alpha_to_digits(text: str) -> str:
    copy = text
    for i, c in enumerate(copy):
        substring = copy[i:]
        for word, digit in NUM_DICT.items():
            if substring.startswith(word):
                copy = copy[:i] + digit + copy[i + 1 :]
    return copy


def solve_b(text: str) -> int:
    lines = text.splitlines()
    result = 0
    for line in lines:
        converted_line = convert_alpha_to_digits(line)
        result += get_digits(converted_line)
    return result


print(f"sample b: {solve_b(sample_b)}")
print(f"solution b: {solve_b(data)}")
