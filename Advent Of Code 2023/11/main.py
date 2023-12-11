# Puzzle:            https://adventofcode.com/2023/day/11
# Video explanation: https://youtu.be/6ThjAxFmYsM

# 1. part - What is the sum of lengths of the shortest path between every pair of galaxies?
with open('input.txt') as f:
    # load the universe data and expand rows with no galaxies
    universe = []
    for line in f.readlines():
        row = list(line.strip())
        universe.append(row)
        if '#' not in row:
            universe.append(row.copy()) # make sure it is a copy

    # find columns with no galaxies
    empty_columns = []
    for x in range(len(universe[0])):
        empty = True
        for y in range(len(universe)):
            if universe[y][x] == '#':
                empty = False
                break
        if empty:
            empty_columns.append(x)

    # expand columns with no galaxies
    for y in range(len(universe)):
        for i, x in enumerate(empty_columns):
            universe[y].insert(i + x, '.')

    # find positions of galaxies in the expanded universe
    galaxies = []
    for y in range(len(universe)):
        for x in range(len(universe[0])):
            if universe[y][x] == '#':
                galaxies.append((x, y))

    # find distances between all pairs of galaxies
    sum_of_lengths = 0
    for a in galaxies:
        for b in galaxies:
            sum_of_lengths += abs(a[0] - b[0]) + abs(a[1] - b[1])

    # divide by 2 because we have added distances from 'a' to 'b' and from 'b' to 'a'
    print(sum_of_lengths//2)

# 2. part - What is the sum of lengths of the shortest path between every pair of galaxies?
from bisect import bisect

with open('input.txt') as f:
    # load the universe data and find rows with no galaxies
    universe = []
    empty_rows = []
    for i, line in enumerate(f.readlines()):
        row = list(line.strip())
        universe.append(row)
        if '#' not in row:
            empty_rows.append(i)

    # find columns with no galaxies
    empty_columns = []
    for x in range(len(universe[0])):
        empty = True
        for y in range(len(universe)):
            if universe[y][x] == '#':
                empty = False
                break
        if empty:
            empty_columns.append(x)
    
    # find positions of galaxies in the expanded universe
    galaxies = []
    expansion_constant = 1000000 - 1 # -1 because we replace emtpy row/column
    for y in range(len(universe)):
        for x in range(len(universe[0])):
            if universe[y][x] == '#':
                dx = expansion_constant * bisect(empty_columns, x)
                dy = expansion_constant * bisect(empty_rows, y)

                galaxies.append((x + dx, y + dy))

    # find distances between all pairs of galaxies
    sum_of_lengths = 0
    for a in galaxies:
        for b in galaxies:
            sum_of_lengths += abs(a[0] - b[0]) + abs(a[1] - b[1])

    # divide by 2 because we have added distances from 'a' to 'b' and from 'b' to 'a'
    print(sum_of_lengths // 2)

# 1. and 2. part combined
from bisect import bisect

with open('input.txt') as f:
    universe = [list(line.strip()) for line in f.readlines()]
    empty_rows = [i for i, row in enumerate(universe) if '#' not in row]
    empty_columns = [x for x in range(len(universe[0])) if all(row[x] != '#' for row in universe)]
    
    for e in [1, 1000000 - 1]:
        galaxies = [(x + e * bisect(empty_columns, x), y + e * bisect(empty_rows, y))
              for y, row in enumerate(universe) for x, c in enumerate(row) if c == '#']
        
        print(sum(abs(a[0] - b[0]) + abs(a[1] - b[1]) for a in galaxies for b in galaxies) // 2)
