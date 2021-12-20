import re
from collections import Counter
import statistics

def parse_data(content:str):

    data = [int(item) for item in content.strip().split(",")]
    return data

def calculate_cost(position, data):    
    cost = 0
    for pos in data:
        cost += abs(pos - position)
    return cost
    
def calculate_cost_part2(position, data):
    cost = 0
    for pos in data:
        distance = abs(pos - position)      
        cost += (distance * (distance + 1))/2
    return cost    

def part1(data: list):
   
    start = min(data)
    end = max(data)
    
    best_position_cost = calculate_cost(start, data)
    best_position = 0
    for position in range(start, end+1):
        cost = calculate_cost(position, data)
        
        print(f"position {position}, cost {cost}")
        if cost < best_position_cost:
            best_position_cost = cost
            best_position = position
            
    print(f"best position {best_position}, cost {best_position_cost}")
    

def part2(data: list):
    
    start = min(data)
    end = max(data)
    
    best_position_cost = calculate_cost_part2(start, data)
    best_position = 0
    for position in range(start, end+1):
        cost = calculate_cost_part2(position, data)
        
        print(f"position {position}, cost {cost}")
        if cost < best_position_cost:
            best_position_cost = cost
            best_position = position
            
    print(f"best position {best_position}, cost {best_position_cost}")


if __name__ == "__main__":

    with open ("data/day7.txt") as f:
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

