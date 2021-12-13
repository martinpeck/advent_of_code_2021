from collections import Counter

def parse_diagnostic(command:str):
    parts = list(map(int,command.strip()))
    return parts
   
    
def determine_most_common_value(data:list, position:int):
    c = Counter([item[position] for item in data])
    
    most_common = c.most_common()
    if len(most_common) > 1 and most_common[0][1] == most_common[1][1]:
        return 1

    return most_common[0][0]
    

def determine_least_common_value(data:list, position:int):
    if determine_most_common_value(data, position) == 1:
        return 0
    else:
        return 1

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
        
print(f"most common: {most_sig_bits}")
print(f"least common: {least_sig_bits}")

gamma = sum([b<<i for i, b in enumerate(most_sig_bits[::-1])])
epsilon = sum([b<<i for i, b in enumerate(least_sig_bits[::-1])])

print(f"gamma: {gamma}")
print(f"epsilon: {epsilon}")
print(f"result: {gamma * epsilon}")

# part 2



# oxygen
oxygen_candidates = data.copy()

for bit in range(len(data[0])):
    
    filter = determine_most_common_value(oxygen_candidates, bit)

    new_o2_candidates = []
    for candidate in oxygen_candidates:
        if candidate[bit] == filter:
            new_o2_candidates.append(candidate)
        
    if len(new_o2_candidates) == 1:
        break
    else:
        oxygen_candidates = new_o2_candidates

assert(len(new_o2_candidates)==1)

o2 = sum([b<<i for i, b in enumerate(new_o2_candidates[0][::-1])])
print(new_o2_candidates[0])
print(o2)
    
# co2
co2_candidates = data.copy()

for bit in range(len(data[0])):
    
    filter = determine_least_common_value(co2_candidates, bit)
    
    new_co2_candidates = []
    for candidate in co2_candidates:
        if candidate[bit] == filter:
            new_co2_candidates.append(candidate)
        
    if len(new_co2_candidates) == 1:
        break
    else:
        co2_candidates = new_co2_candidates

assert(len(new_co2_candidates)==1)

co2 = sum([b<<i for i, b in enumerate(new_co2_candidates[0][::-1])])
print(new_co2_candidates[0])
print(co2)


print(o2*co2)
