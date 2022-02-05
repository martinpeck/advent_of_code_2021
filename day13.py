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
        
    for fold in folds[:1]:        
        for pos, coord in enumerate(points):
            
            if fold[0] == "x" and coord[0] > fold[1]:
                points[pos] = (fold[1]- (coord[0] - fold[1]), coord[1])
            
            if fold[0] == "y" and coord[1] > fold[1]:         
                points[pos] = (coord[0], fold[1] - (coord[1] - fold[1]))
                        
    final_set = set()
            
    for point in points:
        final_set.add(point)
    
    print(f"number of points = {len(final_set)}")


def part2(points: list[tuple[int, int]], folds: list):

    pass


if __name__ == "__main__":

    with open ("data/day13.txt") as f:
        points, folds = parse_data(f.readlines())

    print("🦑 🐬 Part1 🐬 🦑")
    print()
    part1(points, folds) 
    print()
    print("🐟 🐠 🐡 🐟 🐠 🐡")

    print()
    print("🦑 🐬 Part2 🐬 🦑")
    print()
    part2(points, folds)
    print()
    print("🐟 🐠 🐡 🐟 🐠 🐡")

