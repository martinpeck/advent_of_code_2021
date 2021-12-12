with open ("data/day1a.txt") as f:
    data = list(map(int, f.readlines()))

increase_count = 0

for counter, line in enumerate(data):
    if counter > 0:
        if line > data[counter-1]:
            increase_count += 1

print(f"part 1: {increase_count}")

import queue
q = queue.Queue(3)

increase_count = 0

for line in data:

    if q.full():
        value = q.get()
        if value < line:
          increase_count += 1

    q.put(line, block=False)

print(f"part 2: {increase_count}")
