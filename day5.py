import re

def parse_data(lines:list):

    p = re.compile("(\d+),(\d+) -> (\d+),(\d+)")

    for line in lines:
        m = p.search(line)
        yield [(int(m.group(1)), int(m.group(2))),(int(m.group(3)), int(m.group(4)))]

def generate_line_from_points(point_from, point_to):
    
    x1, y1 = point_from
    x2, y2 = point_to
    
    if x1 == x2 or y1 == y2:
        
        if x1 > x2:
            x1, x2 = x2, x1

        if y1 > y2:
            y1, y2 = y2, y1
                
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                yield (x, y)
    
def place_points_on_board(points):
    pass

def part1(data: list):
    
    # fill the board
    for item in data:
        from_position = item[0]
        to_position = item[1]
        
        points = generate_line_from_points(from_position, to_position)
        
        board = place_points_on_board(points)
        
        print(f"fill the board from {from_position} to {to_position} with line of points {list(points)}")


def part2(data: list):
    pass


if __name__ == "__main__":

    with open ("data/day5-test.txt") as f:
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



