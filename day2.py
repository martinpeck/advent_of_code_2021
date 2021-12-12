def parse_command(command:str):
    parts = command.split(" ")
    return (parts[0], int(parts[1]))

depth = 0
horizonal = 0

with open ("data/day2.txt") as f:
    data = list(map(parse_command, f.readlines()))

for command, value in data:
    if command == "down":        
        depth += value
    elif command == "up":
        depth -= value
    elif command == "forward":
        horizonal += value
    
print("Part 1")
print(f"depth: {depth}")
print(f"horizonal: {horizonal}")
print(f"solution: {depth * horizonal}")
print()

depth = 0
horizonal = 0
aim=0
   
for command, value in data:
    if command == "down":   
        aim += value
    elif command == "up":
        aim -= value
    elif command == "forward":
        horizonal += value
        depth += aim * value

print("Part 2")
print(f"depth: {depth}")
print(f"horizonal: {horizonal}")
print(f"solution: {depth * horizonal}")
print()