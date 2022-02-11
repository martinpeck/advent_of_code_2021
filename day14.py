from collections import deque, defaultdict, Counter

import plotext as plt


def parse_data(data: list[str]):

    starting_polymer = ""
    rules = {}
    
    for row_number, row in enumerate([row.strip() for row in data]):
        if row_number == 0:
            starting_polymer = row
        elif row_number >= 2:
            rule_parts = row.split(" -> ")
            rules[rule_parts[0]] = rule_parts[1]

    return starting_polymer, rules


def part1(base_polymer :str, polymer_rules :dict[str, str]):
    print(f"{base_polymer=}")
    print(f"{polymer_rules=}")


def part2(points: list[tuple[int, int]], folds: list):
    pass
    

if __name__ == "__main__":

    with open("data/day14-test.txt") as f:
        starting_polymer, rules = parse_data(f.readlines())

    print("🦑 🐬 Part1 🐬 🦑")
    print()
    part1(starting_polymer, rules)
    print()
    print("🐟 🐠 🐡 🐟 🐠 🐡")

    print()
    print("🦑 🐬 Part2 🐬 🦑")
    print()
    part2(starting_polymer, rules)
    print()
    print("🐟 🐠 🐡 🐟 🐠 🐡")
