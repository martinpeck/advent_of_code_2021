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
    
    result = []
    rows = len(data)
    cols = len(data[0])
    
    for r in range(rows):
        for c in range(cols):
            point = data[r][c]
                        
            left  = 10 if c == 0 else data[r][c-1]
            right = 10 if c == cols - 1 else data[r][c+1] 
            up    = 10 if r == 0 else data[r-1][c]
            down  = 10 if r == rows - 1 else data[r+1][c]
            
            if point < left and point < right and point < up and point < down:
                result.append(point + 1)
            
    print(f"{sum(result)}")
                      

def part2(data: list):
    
    pass        

if __name__ == "__main__":

    with open ("data/day9.txt") as f:
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

