# Puzzle:            https://adventofcode.com/2023/day/6
# Video explanation: https://youtu.be/h_rGq_PUCjo

import math

FILE = 'input.txt'

# 1. part - Determine the number of ways you could beat the record in each race and multiply them together.
with open(FILE) as f:
    times = list(map(int, f.readline().split()[1:]))
    distances = list(map(int, f.readline().split()[1:]))

    result  = 1

    # brute force
    for i in range(len(times)):
        time, distance = times[i], distances[i]

        no_ways = 0
        for speed in range(time):
            if speed * (time - speed) > distance:
                no_ways += 1
        
        result *= no_ways
        no_ways = 0

    print(result)

# 2. part - How many ways can you beat the record in this one much longer race?
with open(FILE) as f:
    time = int("".join(f.readline().split()[1:]))
    distance = int("".join(f.readline().split()[1:]))

    # # We can just brute force it in 8s
    # no_ways = 0
    # for speed in range(time):
    #     if speed * (time - speed) > distance:
    #         no_ways += 1
    # print(no_ways)


    # -x^2 + time * x - distance > 0

    #         -b +- sqrt(b^2 - 4ac)
    # x_1,2 = ---------------------
    #                  2a
    x1 = (-time + math.sqrt(time**2 - 4*distance)) / -2
    x2 = (-time - math.sqrt(time**2 - 4*distance)) / -2

    x1 = math.ceil(x1) if not x1.is_integer() else int(x1) + 1
    x2 = math.floor(x2) if not x2.is_integer() else int(x2) - 1

    print(x2 - x1 + 1)