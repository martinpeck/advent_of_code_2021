def parse_diagnostic(command:str):
    parts = list(map(int,command.strip()))
    return parts

with open ("data/day3.txt") as f:
    data = list(map(parse_diagnostic, f.readlines()))

running_total = [0] * len(data[0])
diagnostic_values = 0

for diagnostic in data:
    diagnostic_values += 1
    for position, bit_value in enumerate(diagnostic):
        if bit_value == 1:
            running_total[position] += 1
            
print(running_total)
print(diagnostic_values)

most_sig_bits = [0] * len(data[0])
least_sig_bits = [0] * len(data[0])

for position, total in enumerate(running_total):
    if total > diagnostic_values/2:
        most_sig_bits[position] = 1
    else:        
        least_sig_bits[position] = 1
        
print(most_sig_bits)
print(least_sig_bits)

gamma = sum([b<<i for i, b in enumerate(most_sig_bits[::-1])])
epsilon = sum([b<<i for i, b in enumerate(least_sig_bits[::-1])])

print(f"gamma: {gamma}")
print(f"epsilon: {epsilon}")
print(f"result: {gamma * epsilon}")