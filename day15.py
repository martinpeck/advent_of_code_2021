from dataclasses import dataclass
import random
from collections import deque, defaultdict
from sty import bg, ef, fg


@dataclass
class Grid:
    risks: dict
    rows: int
    cols: int


def print_grid(grid: Grid, costs: dict = None):

    path = set()

    costs_output = []
    for r in range(grid.rows):        
        grid_line = ""
        cost_line = ""
        
        for c in range(grid.cols):

            highlight = random.random() > 0.5
            highlight = False
            
            if highlight:
                grid_line += bg.blue + ef.b + str(grid.risks[(r, c)]) + ef.rs + bg.rs
            else:
                grid_line += fg.da_grey + str(grid.risks[(r, c)]) + fg.rs

            if costs:
                cost_line += "{:03d} ".format(costs[r, c])
            else:
                cost_line = ""
        
        print(f"{grid_line}")
        if costs:
            costs_output.append(cost_line)
            
    if costs:
        print()
        for line in costs_output:
            print(f"{line}")


def parse_data(data: list[str]) -> list[list[str]]:

    risks = {}
    for r, row in enumerate([row.strip() for row in data]):
        for c, col_value in enumerate([int(col) for col in row]):
            risks[(r, c)] = col_value

    grid = Grid(risks, r + 1, c + 1)
    return grid


def expand_grid(original_grid: Grid, scale_factor : int = 5) -> Grid:
    
    new_grid = Grid(risks={}, rows = original_grid.rows * scale_factor, cols = original_grid.cols * scale_factor)
    for x in range(0, scale_factor):
        for y in range(0, scale_factor):
            for row in range(original_grid.rows):
                for col in range(original_grid.cols):
                    new_row = row + (original_grid.rows * x)
                    new_col = col + (original_grid.cols * y)
                    
                    original_risk = original_grid.risks[row, col]
                    new_risk = original_risk + x + y
                    if new_risk > 9:
                        new_risk = new_risk - 9
                    new_grid.risks[(new_row, new_col)] = new_risk
            
    return new_grid


def get_neighbours(current_position: tuple[int, int], grid: Grid):

    # north, east, south, west
    for delta in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        new_position = (current_position[0] + delta[0], current_position[1] + delta[1])
        if new_position in grid.risks.keys():
            yield new_position


def solve_grid(grid: Grid):
    visited = set()
    costs = defaultdict(lambda: -1)
    costs[(0, 0)] = 0

    frontier = deque()
    frontier.append((0, 0))

    while len(frontier) > 0:
        current_position = frontier.popleft()
        visited.add(current_position)
        current_position_cost = costs[current_position]

        # get all neighbours
        for neighbour in get_neighbours(current_position, grid):

            current_neighbour_cost = costs[neighbour]
            new_neighbour_cost = current_position_cost + grid.risks[neighbour]

            if current_neighbour_cost < 0 or (new_neighbour_cost < current_neighbour_cost):
                costs[neighbour] = new_neighbour_cost
                if neighbour in visited:
                    visited.remove(neighbour)

            if neighbour not in visited:
                visited.add(neighbour)
                frontier.append(neighbour)
    
    return costs

def part1(grid: Grid):
    costs = solve_grid(grid)
    print_grid(grid, costs)


def part2(grid: list[list[int]]):
    new_grid = expand_grid(grid)
    costs = solve_grid(new_grid)
    print_grid(new_grid, costs)


if __name__ == "__main__":

    with open("data/day15.txt") as f:
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
