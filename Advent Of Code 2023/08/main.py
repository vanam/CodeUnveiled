# Puzzle:            https://adventofcode.com/2023/day/8
# Video explanation: https://youtu.be/VI6tM72Jrgk

# 1. part - ow many steps are required to reach ZZZ?
import re

FILE = 'input.txt'

MAP = {}

with open(FILE) as f:
    instructions = f.readline()
    f.readline() # skip empty line

    for line in f.readlines():
       u, a, b =  re.search(r'(\w+) = \((\w+), (\w+)\)', line).groups()
       MAP[u] = {'L': a, 'R': b}

    node = 'AAA' # start
    steps = 0
    while node != 'ZZZ': # we found the end
        i = steps % (len(instructions) - 1) # repeat the whole sequence of instructions as necessary
        node = MAP[node][instructions[i]]
        steps += 1

    print(steps)

# 2. part - How many steps does it take before you're only on nodes that end with Z?
import re
from functools import reduce

FILE = 'input.txt'

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def lcm(a, b):
    return a * (b // gcd(a, b))

MAP = {}

with open(FILE) as f:
    instructions = f.readline()
    f.readline() # skip empty line

    starts = []
    for line in f.readlines():
       u, a, b =  re.search(r'(\w+) = \((\w+), (\w+)\)', line).groups()
       MAP[u] = {'L': a, 'R': b}
       if u[-1] == 'A':
           starts.append(u)
    
    ends = []
    for node in starts:
        steps = 0
        while node[-1] != 'Z': # we found the end
            i = steps % (len(instructions) - 1) # repeat the whole sequence of instructions as necessary
            node = MAP[node][instructions[i]]
            steps += 1
        ends.append(steps)

    print(reduce(lcm, ends))
