import re

def parse_data(lines:list):

    p = re.compile("(\d+),(\d+) -> (\d+),(\d+)")

    for line in lines:
        m = p.search(line)
        yield [(int(m.group(1)), int(m.group(2))),(int(m.group(3)), int(m.group(4)))]


def part1(data: list):
    
    # fill the board
    for item in data:
        from_position = item[0]
        to_position = item[0]
        
        print(f"fill the board from {from_position} to {to_position}")


def part2(data: list):
    pass


if __name__ == "__main__":

    with open ("data/day5.txt") as f:
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



