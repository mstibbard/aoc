import networkx as nx
from aocd import get_data
from dotenv import load_dotenv

load_dotenv()
data = get_data(day=5, year=2024)
samp = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""


def is_valid_order(graph, update):
    """Iterates through an 'update' checking for any paths that are going backwards according to the graph."""
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            if nx.has_path(graph, update[j], update[i]):
                return False
    return True


def solve_a(inputs):
    orders, updates = inputs.split(sep="\n\n")
    orders = orders.splitlines()
    updates = updates.splitlines()

    G = nx.DiGraph()

    for o in orders:
        x, y = o.split(sep="|")
        G.add_edge(int(x), int(y))

    correct_middle_sum = 0
    for u in updates:
        page_nums = u.split(sep=",")
        page_nums = [int(o) for o in page_nums]
        sg = G.subgraph(page_nums)
        if is_valid_order(sg, page_nums):
            correct_middle_sum += page_nums[len(page_nums) // 2]

    return correct_middle_sum


print(f"sample a: {solve_a(samp)}")
print(f"answer a: {solve_a(data)}\n")


def solve_b(inputs):
    orders, updates = inputs.split(sep="\n\n")
    orders = orders.splitlines()
    updates = updates.splitlines()

    G = nx.DiGraph()

    for o in orders:
        x, y = o.split(sep="|")
        G.add_edge(int(x), int(y))

    incorrect_middle_sum = 0
    for u in updates:
        page_nums = u.split(sep=",")
        page_nums = [int(o) for o in page_nums]
        sg = G.subgraph(page_nums)
        if not is_valid_order(sg, page_nums):
            ordered = list(nx.topological_sort(sg))
            incorrect_middle_sum += ordered[len(ordered) // 2]

    return incorrect_middle_sum


print(f"sample b: {solve_b(samp)}")
print(f"answer b: {solve_b(data)}")
