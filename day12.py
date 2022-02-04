from collections import deque, defaultdict

def parse_data(data:list[str]):

    cave_system = defaultdict(list[str])
    
    for row in data:
        nodes = row.strip().split("-")
        from_node = nodes[0]
        to_node = nodes[1]
        cave_system[from_node].append(to_node)
        cave_system[to_node].append(from_node)

    return cave_system


def part1(cave_system: list):

    solution_paths = []
    
    search_queue = deque()    
    search_queue.append(["start"])
    
    while len(search_queue) > 0:
        
        path : list[str] = search_queue.popleft()        
        current_cave = path[-1]        
        connecting_caves = cave_system[current_cave]
                
        for cave in connecting_caves:
            new_path = path + [cave]            
            if cave == "start":
                pass
            elif cave == "end":
                solution_paths.append(new_path)
            elif cave.isupper():
                search_queue.append(new_path)
            elif cave.islower() and cave not in path:
                search_queue.append(new_path)
        
    return solution_paths


def part2(data: list, paths: list):
    
    pass


if __name__ == "__main__":

    with open ("data/day12.txt") as f:
        data = parse_data(f.readlines())

    print("🦑 🐬 Part1 🐬 🦑")
    print()
    paths = part1(data)
    print(f"number of solution paths: {len(paths)}")
    print()
    print("🐟 🐠 🐡 🐟 🐠 🐡")

    print()        
    print("🦑 🐬 Part2 🐬 🦑")
    print()
    part2(data, paths)
    print()
    print("🐟 🐠 🐡 🐟 🐠 🐡")

