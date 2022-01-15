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
                result.append((r, c))
    
    total = 0
    for row, col in result:
        total += data[row][col] + 1
        
    print(total)
            
    return result
                      
def size_basin(data: list, row: int, col: int) -> int:
    
    rows = len(data)
    cols = len(data[0])
    search_space = deque()
    search_space.append((row, col))
    
    basin_members = set()
    
    while len(search_space) > 0:
        row, col = search_space.popleft()
        
        basin_members.add((row, col))
        
        for neighbour_row, neighbour_col in [(row, col - 1), (row, col+1), (row - 1, col), (row + 1, col)]:
            if neighbour_row >= 0 and neighbour_col >= 0 and neighbour_row < rows and neighbour_col < cols:
                if data[neighbour_row][neighbour_col] > data[row][col] and data[neighbour_row][neighbour_col] < 9:
                    search_space.append((neighbour_row, neighbour_col))
        
    return len(basin_members)
    
    

def part2(data: list, part1_results: list):
    
    sizes = []
    for row, col in part1_results:
        sizes.append(size_basin(data, row, col))
    
    print((prod(sorted(sizes,reverse=True)[:3])))
               

if __name__ == "__main__":

    with open ("data/day9.txt") as f:
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

