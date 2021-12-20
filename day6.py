import re
from collections import defaultdict
from collections import Counter
from types import new_class

def parse_data(content:str):

    data = [int(item) for item in content.strip().split(",")]
    return data


def part1(data: list):

    for day in range(80):
        new_state = []

        for fish in data:
            if fish == 0:
                new_state.append(6)
                new_state.append(8)
            else:
                new_state.append(fish - 1)

        data = new_state

    print(f"Number of fish: {len(data)}")



def part2(data: list):
    pass


if __name__ == "__main__":

    with open ("data/day6.txt") as f:
        data = parse_data(f.read())

    print("🦑 🐬 Part1 🐬 🦑")
    print()
    part1(data)
    print()
    print("🐟 🐠 🐡 🐟 🐠 🐡")

    print()

    print("🦑 🐬 Part2 🐬 🦑")
    print()
    part2(data)
    print()
    print("🐟 🐠 🐡 🐟 🐠 🐡")
