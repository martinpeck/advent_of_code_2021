import random
from sty import bg, ef, fg


def print_grid(grid: list[list[str]]):
    
    for row in grid:
        for col in row:
            
            highlight = random.random() < .5
            
            if highlight:
                print(f"{bg.blue}{ef.b}{col}{ef.rs}{bg.rs}", end='')
            else:
                print(f"{fg.da_grey}{col}{fg.rs}", end='')
        print()
            

def parse_data(data: list[str]) -> list[list[str]]:

    grid = []
    for row in [row.strip() for row in data]:
        grid.append([int(col) for col in row])
        
    return grid


def part1(grid: list[list[int]]):
    
    print_grid(grid)


def part2(grid: list[list[int]]):
    pass


if __name__ == "__main__":

    with open("data/day15-test.txt") as f:
        grid = parse_data(f.readlines())

    print("🦑 🐬 Part1 🐬 🦑")
    print()
    part1(grid)
    print()
    print("🐟 🐠 🐡 🐟 🐠 🐡")

    print()
    print("🦑 🐬 Part2 🐬 🦑")
    print()
    part2(grid)
    print()
    print("🐟 🐠 🐡 🐟 🐠 🐡")
