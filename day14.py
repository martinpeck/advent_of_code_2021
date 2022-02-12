from collections import deque, defaultdict, Counter
from copy import copy
from typing import Iterator


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


def pairwise(iterable):

    a : Iterator = iter(iterable)

    try:
        first = a.__next__()

        while True:
            second = a.__next__()
            yield first + second
            first = second

    except StopIteration:
        pass


def count_them(iteration, polymer_to_count):
    c = Counter(polymer_to_count)
    most_common = c.most_common(1)[0]
    least_common = c.most_common()[-1]
    print(f"{iteration=} {most_common=} {least_common=} {most_common[1] - least_common[1]}")

def part1(base_polymer :str, polymer_rules :dict[str, str]):

    new_polymer = base_polymer

    for i in range(10):
        base_polymer = new_polymer
        new_polymer = ""
        for pair in pairwise(base_polymer):
            element_to_insert = polymer_rules[pair]
            new_polymer += pair[0]
            new_polymer += element_to_insert

        new_polymer += pair[1]

    count_them(i, new_polymer)


def part2(base_polymer :str, polymer_rules :dict[str, str]):

    first_element = base_polymer[0]

    polymer_pairs = defaultdict(int)

    for pair in pairwise(base_polymer):
        polymer_pairs[pair] += 1

    for iteration in range(40):
        pairs = [item for item in polymer_pairs.items() if item[1] > 0]

        for elements, instances in pairs:
            new_element = polymer_rules[elements]

            new_pair_one = elements[0] + new_element
            new_pair_two = new_element + elements[1]

            polymer_pairs[new_pair_one] += instances
            polymer_pairs[new_pair_two] += instances
            polymer_pairs[elements] -= instances

    totals = Counter()

    totals[first_element] += 1

    for pair_with_count in [item for item in polymer_pairs.items() if item[1] > 0]:
        # only count the second item in each pair
        totals[pair_with_count[0][1]] += pair_with_count[1]

    most_common = totals.most_common(1)[0]
    least_common = totals.most_common()[-1]

    print(f"{iteration=} {most_common=} {least_common=} {most_common[1] - least_common[1]}")


if __name__ == "__main__":

    with open("data/day14.txt") as f:
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
