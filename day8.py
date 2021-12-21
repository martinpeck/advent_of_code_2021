import re
from collections import Counter
import statistics

def parse_data(data:list):

    parsed_data = []
    for row in data:
        sides = [part.strip() for part in row.split("|")]
        parsed_data.append((sides[0].split(" "),sides[1].split(" ")))
          
    return parsed_data


def detect_digit(pattern: str):
    
    unique_chars = set(pattern)
    length_set = len(unique_chars)
    
    print(f"unique {unique_chars}, length of set: {length_set}")
    if length_set == 2:
        return 1
    elif length_set == 4:
        return 4
    elif length_set == 3:
        return 7
    elif length_set == 7:
        return 8
    else:
        return None
    
def part1(data: list):
    
    total = 0
    
    for line in data:
        for pattern in line[1]:
            if detect_digit(pattern) in [1,4,7,8]:
                total += 1
                
    print(total)
                    


def part2(data: list):
    pass


if __name__ == "__main__":

    with open ("data/day8.txt") as f:
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

