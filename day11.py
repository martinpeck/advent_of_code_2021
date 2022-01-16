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
        parsed_data.append([int(state) for state in row.strip()])

    return parsed_data

def get_all_neighbours(row, col, number_of_rows, number_of_cols):
    if col != 0:
        yield (row, col - 1)
    
    if col < number_of_cols - 1:
        yield (row, col + 1)
    
    if row != 0:
        yield (row - 1, col)
    
    if row < number_of_rows - 1:    
        yield (row + 1, col)
        
    if row != 0 and col != 0:
        yield (row -1, col - 1)
        
    if row < number_of_rows - 1 and col < number_of_cols - 1:        
        yield (row + 1, col + 1)
        
    if row != 0 and col < number_of_cols - 1:                
        yield (row - 1, col + 1)

    if col != 0 and row < number_of_rows - 1:                        
        yield (row + 1, col -1)

def part1(data: list):

    result = None
    
    total_rows = len(data)
    total_cols = len(data[0])
    flash_count = 0 
    flashes = deque()
    
    for step in range(1,101):
        
        print(f"{step=}")
        flashes.clear()
        
        # increase energy by 1
        for r, row in enumerate(data):
            for c, col in enumerate(row):                
                new_energy_value = col + 1
                
                data[r][c] = new_energy_value                
                if new_energy_value > 9:
                    flashes.append((r, c))
                
        # deal with flashes
        while len(flashes) > 0:
            
            flash_row, flash_col = flashes.popleft()
                        
            if data[flash_row][flash_col] == 0:
                continue
            
            data[flash_row][flash_col] = 0
            flash_count += 1
            
            neighbours = list(get_all_neighbours(flash_row, flash_col, total_rows, total_cols))
            for neighbour_row, neighbour_col in neighbours:
                neighbour_value = data[neighbour_row][neighbour_col]
                if neighbour_value != 0:
                    neighbour_value += 1
                    if neighbour_value > 9:
                        flashes.append((neighbour_row, neighbour_col))
                    data[neighbour_row][neighbour_col] = neighbour_value
        
    print(f"{data=}")
    print(f"{flash_count=}")
    
    return result


def part2(data: list, part1_results: list):
    pass

if __name__ == "__main__":

    with open ("data/day11.txt") as f:
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

