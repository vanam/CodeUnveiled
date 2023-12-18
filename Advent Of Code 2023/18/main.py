# Puzzle:            https://adventofcode.com/2023/day/18
# Video explanation: https://youtu.be/nz8YxWVj-wI

# 1. part - How many cubic meters of lava could the lagoon hold?
DIRECTION = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}

def area(points):
    """"Shoelace formula"""""
    result = 0
    for i in range(len(points) -1):
        x1, y1 = points[i]
        x2, y2 = points[i+1]
        result += x1 * y2 - x2*y1

    return abs(result) // 2

with open('input.txt') as f:
    dig_plan = [line.split() for line in f.readlines()]

    perimeter = 0
    
    points = [(0, 0)]
    for inst in dig_plan:
        dist = int(inst[1])
        dir = DIRECTION[inst[0]]
        
        perimeter += dist

        # from the last point we move n steps in a specified direction
        points.append((points[-1][0] + dist * dir[0], points[-1][1] + dist * dir[1]))

    # A = i + b/2 - 1            i: number interior points    b: number of boundary points
    # i = A - b/2 + 1
        
    # We are looking for i + b
    # i + b = A - b/2 + 1 + b = A + b/2 + 1
    print(area(points) + perimeter // 2 + 1)

# 2. part - How many cubic meters of lava could the lagoon hold?
DIRECTION = {"0": (1, 0), "1": (0, 1), "2": (-1, 0), "3": (0, -1)}

def area(points):
    """Shoelace formula"""
    result = 0
    for i in range(len(points) -1):
        x1, y1 = points[i]
        x2, y2 = points[i+1]
        result += x1 * y2 - x2*y1

    return abs(result) // 2

with open('input.txt') as f:
    dig_plan = [line.split() for line in f.readlines()]

    perimeter = 0

    points = [(1, 1)]
    for inst in dig_plan:
        dist = int(inst[2][2:7], 16) # distance in hexadecimal
        dir = DIRECTION[inst[2][-2]]
        
        perimeter += dist

        # from the last point we move n steps in a specified direction
        points.append((points[-1][0] + dist * dir[0], points[-1][1] + dist * dir[1]))

    # A = i + b/2 - 1            i: number interior points    b: number of boundary points
    # i = A - b/2 + 1
        
    # We are looking for i + b
    # i + b = A - b/2 + 1 + b = A + b/2 + 1
    print(area(points) + perimeter // 2 + 1)