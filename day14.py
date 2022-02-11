from collections import deque, defaultdict, Counter
from typing import Iterator

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
    
    c = Counter(new_polymer)
    
    most_common = c.most_common(1)[0]
    least_common = c.most_common()[-1]
    
    print(f"{most_common=} {least_common=} {most_common[1] - least_common[1]}")



def part2(points: list[tuple[int, int]], folds: list):
    pass
    

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
