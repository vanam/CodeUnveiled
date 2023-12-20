# Puzzle:            https://adventofcode.com/2023/day/19
# Video explanation: https://youtu.be/tvyvJ0CqnXo

# 1. part - What is the sum of the rating numbers of accepted parts?
import re

with open('input.txt') as f:
    workflow_lines, part_lines = f.read().split("\n\n")

    # parse the workflows
    workflows = {}
    for line in workflow_lines.split():
        name, rules = re.findall(r"(\w+)\{(.*?)\}", line)[0]
        workflows[name] = rules.split(",")

    # parse and rate the parts
    rating_number_sum = 0
    for line in part_lines.split():
        # parse the part eg: {'x': 787, 'm': 2655, 'a': 1222, 's': 2876}
        part = dict([(k, int(v)) for k, v in re.findall(r"(\w)=(\d+)", line)])
        
        wf = 'in' # begin in the workflow named 'in'
        while wf not in ['A', 'R']:
            for rule in workflows[wf]:
                # parse if rule is a condition
                if ":" in rule:
                    category, op, threshold, cond_wf = re.findall(r"(\w)([><])(\d+):(\w+)", rule)[0]
                    threshold = int(threshold)

                    # if the condition is true
                    if (op == "<" and part[category] < threshold) or (op == ">" and part[category] > threshold):
                        wf = cond_wf
                        break
                else:
                    wf = rule
                
        if wf == "A":
            rating_number_sum += sum(part.values())
    print(rating_number_sum)

# 2. part - How many distinct combinations of ratings will be accepted by the Elves' workflows?
import re

with open('input.txt') as f:
    workflow_lines, _ = f.read().split("\n\n")

    # parse the workflows
    workflows = {}
    for line in workflow_lines.split():
        name, rules = re.findall(r"(\w+)\{(.*?)\}", line)[0]
        workflows[name] = rules.split(",")

    # find ranges of category values which get accepted
    parts = []
    part = {"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)}

    # traverse the workflow tree
    nodes = [("in", part)]

    while len(nodes) > 0:
        wf, part = nodes.pop()

        # try all the
        for rule in workflows[wf]:
            # note that 'part' is modified by each rule

            # parse if rule is a condition
            if ":" in rule:
                category, op, threshold, cond_wf = re.findall(r"(\w)([><])(\d+):(\w+)", rule)[0]
                threshold = int(threshold)

                # part which will fulfill the condition 
                cond_part = part.copy()
                
                if op == '<':
                    cond_part[category] = (cond_part[category][0], threshold - 1)
                    part[category] = (int(threshold), part[category][1])
                elif op == '>':
                    cond_part[category] = (int(threshold) + 1, cond_part[category][1])
                    part[category] = (part[category][0], int(threshold))

                if cond_wf in ["A", "R"]:
                    if cond_wf == "A":
                        parts.append(cond_part.copy())
                else:
                    # branch out by fulfilling the condition
                    nodes.append((cond_wf, cond_part.copy()))
            else:
                if rule in ["A", "R"]:
                    if rule == "A":
                        parts.append(part.copy())
                else:
                    nodes.append((rule, part.copy()))

    # calculate possible combinations
    all_combinations = 0
    for part in parts:
        combinations = 1
        for v in part.values():
            combinations *= v[1] - v[0] + 1
        all_combinations += combinations
    print(all_combinations)