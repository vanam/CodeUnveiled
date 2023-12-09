# Puzzle:            https://adventofcode.com/2023/day/4
# Video explanation: https://youtu.be/E-nCzSN_LCY

# 1. part - How many points are they worth in total?
FILE = 'input.txt'

with open(FILE) as f:
    lines = f.readlines()
    total_points = 0

    for line in lines:
        parts = line.split(": ")[1].split("|")
        winning_numbers = set(map(int, parts[0].split()))
        card_numbers = set(map(int, parts[1].split()))

        no_winning = len(winning_numbers.intersection(card_numbers))

        # 0 or 2^(N-1)
        total_points += 2**(no_winning-1) if no_winning > 0 else 0

    print(total_points)

# 2. part - How many total scratchcards do you end up with?
from collections import defaultdict 

FILE = 'input.txt'

# at the beginning we have one of each card
scratchcard_count = defaultdict(lambda: 1)

with open(FILE) as f:
    lines = f.readlines()
    total_scratchcards = 0

    for i, line in enumerate(lines, 1):
        parts = line.split(": ")[1].split("|")
        winning_numbers = set(map(int, parts[0].split()))
        card_numbers = set(map(int, parts[1].split()))

        no_winning = len(winning_numbers.intersection(card_numbers))

        # add number of scratchcards with number i
        total_scratchcards += scratchcard_count[i]
        
        # add copies of N following cards
        for j in range(i + 1, i + 1 + no_winning):
            scratchcard_count[j] += scratchcard_count[i]

    print(total_scratchcards)