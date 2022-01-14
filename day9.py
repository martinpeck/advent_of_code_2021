import re
from collections import Counter
import statistics
from typing import KeysView

def parse_data(data:list):

    parsed_data = []
    for row in data:     
        parsed_data.append([int(n) for n in row.strip()])
          
    return parsed_data



def part1(data: list):
    for row in data:
        print(row)


def part2(data: list):
    
    pass        

if __name__ == "__main__":

    with open ("data/day9-test.txt") as f:
        data = parse_data(f.readlines())

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

