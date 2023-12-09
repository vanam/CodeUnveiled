# Puzzle:            https://adventofcode.com/2023/day/3
# Video explanation: https://youtu.be/rhHAPcnwU4Y

# 1. part - What is the sum of all of the part numbers in the engine schematic?
FILE = 'input.txt'
DIRECTIONS = [[0,1], [1,0], [0,-1], [-1, 0], [-1,1], [-1,-1], [1,-1], [1,1]]

def number_from_digits(digits: list[str]):
    return int(''.join(digits))

with open(FILE) as f:
    lines = f.readlines()
    part_number_sum = 0
    max_x = len(lines[0].strip())
    max_y = len(lines)
    for i in range(max_y):
        digits = []
        adjacent = False
        for j in range(max_x):
            c = lines[i][j]
            # collect digits which form a number
            if c.isdigit():
                digits.append(c)
                # we already know this number is adjacent to a symbol
                if adjacent:
                    continue
                # look for symbols adjacent to a number
                for dx, dy in DIRECTIONS:
                    x, y = j + dx, i + dy
                    # make sure we stay inside the engine schematic
                    if 0 <= x < max_x and 0 <= y < max_y:
                        c = lines[y][x]
                        # look for symbols which are not a digit or '.'
                        if not adjacent and c != '.' and not c.isdigit():
                            adjacent = True
                            break;
            else:
                if adjacent:
                    part_number_sum += number_from_digits(digits)
                digits = []
                adjacent = False
        # edge case where number ends with the line
        if adjacent:
            part_number_sum += number_from_digits(digits)
    print(part_number_sum)

# 2. part - What is the sum of all of the gear ratios in your engine schematic?
from collections import defaultdict 
FILE = 'input.txt'
DIRECTIONS = [[0,1], [1,0], [0,-1], [-1, 0], [-1,1], [-1,-1], [1,-1], [1,1]]

def number_from_digits(digits: list[str]):
    return int(''.join(digits))

with open(FILE) as f:
    lines = f.readlines()
    gear_ratio_candidates = defaultdict(list) # for symbols '*' at position (x, y) we will keep track of adjacent numbers
    max_x = len(lines[0].strip())
    max_y = len(lines)
    for i in range(max_y):
        digits = []
        adjacent = []
        for j in range(max_x):
            c = lines[i][j]
            # collect digits which form a number
            if c.isdigit():
                digits.append(c)
                # we already know this number is adjacent to a symbol '*'
                if adjacent:
                    continue
                # look for symbols adjacent to a number
                for dx, dy in DIRECTIONS:
                    x, y = j + dx, i + dy
                    # make sure we stay inside the engine schematic
                    if 0 <= x < max_x and 0 <= y < max_y:
                        c = lines[y][x]
                        # look for symbols which is '*'
                        if len(adjacent) == 0 and c == '*':
                            adjacent.append((x, y)) # in part 1 we had a boolean here now we track position of symbol '*'
                            break;
            else:
                if len(adjacent) > 0:
                    part_number = number_from_digits(digits)
                    for xy in adjacent:
                        gear_ratio_candidates[xy].append(part_number)
                digits = []
                adjacent = []
        # edge case where number ends with the line
        if len(adjacent) > 0:
            part_number = number_from_digits(digits)
            for xy in adjacent:
                gear_ratio_candidates[xy].append(part_number)
    # calculate and print sum of gear ratios
    print(sum(gears[0] * gears[1] for gears in gear_ratio_candidates.values() if len(gears) == 2))