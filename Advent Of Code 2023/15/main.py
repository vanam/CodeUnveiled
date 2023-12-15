# Puzzle:            https://adventofcode.com/2023/day/15
# Video explanation: https://youtu.be/6Teg3RGYdDg

# 1. part - What is the sum of the hash results?

from functools import reduce

def hash(string):
    return reduce(lambda value, c: (value + ord(c)) * 17 % 256, string, 0)

with open('input.txt') as f:
    init = f.readline().strip().split(',')

    sum_of_results = sum(hash(step) for step in init)
    print(sum_of_results)

# 2. part - What is the focusing power of the resulting lens configuration?

import re
from functools import reduce
from collections import defaultdict

def hash(string):
    return reduce(lambda value, c: (value + ord(c)) * 17 % 256, string, 0)

with open('input.txt') as f:
    init = [re.split(r"([^a-zA-Z0-9])", step) for step in f.readline().strip().split(',')]

    boxes = defaultdict(list)
    for label, op, fl in init:
        h = hash(label)

        if op == '-':
            # remove the lens with the given label
            boxes[h] = list(filter(lambda e: e[0] != label, boxes[h]))
        elif op == '=':
            # find a position of lens with the given label
            position = -1
            for i in range(len(boxes[h])):
                if boxes[h][i][0] == label:
                    position = i
                    break

            if position != -1:
                # replace the old lens
                boxes[h][position] = (label, fl)
            else:
                # add the lens to the box
                boxes[h].append((label, fl))

    focusing_power = 0
    for no, box in boxes.items():
        for i, slot in enumerate(box, 1):
            focusing_power += (no + 1) * i * int(slot[1])

    print(focusing_power)
