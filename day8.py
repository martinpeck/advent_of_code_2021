import re
from collections import Counter
import statistics
from typing import KeysView

def parse_data(data:list):

    parsed_data = []
    for row in data:
        sides = [part.strip() for part in row.split("|")]
        parsed_data.append((sides[0].split(" "),sides[1].split(" ")))
          
    return parsed_data


def detect_digit(pattern: str):
    
    unique_chars = set(pattern)
    length_set = len(unique_chars)
        
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

def decode_pattern(pattern: list[str]) -> list[set]:
            
    result = ["?"] * 10
        
    for p in sorted(pattern, key=len):
        length = len(p)
        if length==2:
            result[1] = set(p)
        if length==3:
            result[7] = set(p)
        if length==4:
            result[4] = set(p)
        if length==5:            
            if set(p).intersection(result[1]) == result[1]:
                result[3] = set(p)
            elif len(set(p) - result[4]) == 2:
                result[5] = set(p)                
            elif len(set(p) - result[4]) == 3:
                result[2] = set(p)            
        if length==6:
            if set(p).intersection(result[1]) != result[1]:
                result[6] = set(p)
            elif set(p).intersection(result[3]) == result[3]:
                result[9] = set(p)
            else:
                result[0] = set(p)                
        if length==7:
            result[8] = set(p)            
    
    return result

def decode_values(values: list[str], key: list[set]) -> int:
    
    result_string = ""
    for value in values:
        value_set = set(value)
        for num, k in enumerate(key):
            if value_set == k:
                result_string += str(num)
                
    return int(result_string)                    
    

def part1(data: list):
    
    total = 0
    
    for line in data:
        for pattern in line[1]:
            if detect_digit(pattern) in [1,4,7,8]:
                total += 1
                
    print(total)
                    


def part2(data: list):
    
    total = 0
    
    for pattern, values in data:        
        key = decode_pattern(pattern)
        number = decode_values(values, key)
        
        total += number
    
    print(f"{total=}")
        

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

