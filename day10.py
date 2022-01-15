from encodings import search_function
import re
from collections import Counter
import statistics
from typing import KeysView
from collections import deque
from math import prod

def parse_data(data:list):

    parsed_data = []
    for row in data:     
        parsed_data.append(row.strip())
          
    return parsed_data


def part1(data: list):
       
    result = None        
    score = 0
    
    for row in data:
        stack = deque()
        for position, instruction in enumerate(row):
            match instruction:
                case "[":
                    stack.appendleft("]")
                case "<":
                    stack.appendleft(">")
                case "{":
                    stack.appendleft("}")
                case "(":
                    stack.appendleft(")")
                case _:
                    pair = stack.popleft()
                    if pair != instruction:
                        match instruction:
                            case "]":
                                score += 57
                            case ">":
                                score += 25137
                            case "}":
                                score += 1197
                            case ")":
                                score += 3  
                        continue                                     
                                    
    print(f"{score=}")
                
    return result
                          

def part2(data: list, part1_results: list):
    
    pass               

if __name__ == "__main__":

    with open ("data/day10.txt") as f:
        data = parse_data(f.readlines())

    print("🦑 🐬 Part1 🐬 🦑")
    print()
    result_part1 = part1(data)
    print()
    print("🐟 🐠 🐡 🐟 🐠 🐡")

    print()

    print("🦑 🐬 Part2 🐬 🦑")
    print()
    part2(data, result_part1)
    print()
    print("🐟 🐠 🐡 🐟 🐠 🐡")

