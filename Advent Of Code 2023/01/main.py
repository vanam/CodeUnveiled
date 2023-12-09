# Puzzle:            https://adventofcode.com/2023/day/1
# Video explanation: https://youtu.be/L06jq8Tjsjw

# 1. part -  What is the sum of all of the calibration values? (only digits)
FILE = 'input.txt'

with open(FILE) as f:
    sum_of_values = 0
    
    for line in f.readlines():
        digits = []
        for c in line:
            if c.isdigit():
                digits.append(int(c))
        sum_of_values += digits[0] * 10 + digits[-1]

    print(sum_of_values)

# 2. part -  What is the sum of all of the calibration values? (with digits as text)
import re

FILE = 'input.txt'

NUMBERS = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

with open(FILE) as f:
    sum_of_values = 0
    
    for line in f.readlines():
        digits = []

        # must use lookahead assertion" !
        # example: "6oneightsr"
        r = r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))' 
        # ['6', 'one', 'eight']

        # r = r'(one|two|three|four|five|six|seven|eight|nine|\d)'
        # ['6', 'one']   
        
        pattern = re.compile(r)
        for w in pattern.findall(line):
            if w.isdigit():
                digits.append(int(w))
            elif w in NUMBERS:
                digits.append(NUMBERS[w])
        sum_of_values += digits[0] * 10 + digits[-1]

    print(sum_of_values)
