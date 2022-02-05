from collections import deque, defaultdict, Counter

def parse_data(data:list[str]):

    points = []    
    folds = []

    parse_points = True
    for row in [row.strip() for row in data]:        
        if row == "":
            parse_points = False
        elif parse_points:
            coordinates = tuple([int(point) for point in row.split(",")])
            points.append(coordinates)
        elif not parse_points:
            fold_details = row.split("=")
            folds.append((fold_details[0].strip("fold along "), int(fold_details[1])))            
        
    return points, folds


def part1(points: list[tuple[int, int]], folds: list):

    solution = []    
    print(points)
    print(folds)
    return solution


def part2(points: list[tuple[int, int]], folds: list):

    solution = []
    return solution


if __name__ == "__main__":

    with open ("data/day13-test.txt") as f:
        points, folds = parse_data(f.readlines())

    print("🦑 🐬 Part1 🐬 🦑")
    print()
    solution = part1(points, folds)    
    print()
    print("🐟 🐠 🐡 🐟 🐠 🐡")

    print()
    print("🦑 🐬 Part2 🐬 🦑")
    print()
    solution = part2(points, folds)    
    print()
    print("🐟 🐠 🐡 🐟 🐠 🐡")

