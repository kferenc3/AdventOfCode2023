import os
import numpy as np
os.chdir('/Users/ferenc.kiss/AdventOfCode2023/aoc_rust')

test = "Time:      7  15   30\nDistance:  9  40  200"
#inp = [[int(y.strip()) for y in x.strip().split() if y.strip().isdigit()] for x in test.split("\n")]
inp = [[int(y.strip()) for y in x.strip().split() if y.strip().isdigit()] for x in open('inputdata_day6')]
results = []


########
#PART I#
########
for i in range(len(inp[0])):
    racetime = inp[0][i]
    record = inp[1][i]
    win = 0
    for x in range(racetime+1):
        result = x*(racetime-x)
        if result > record:
            win += 1
    results.append(win)

print(np.prod(results))

#########
#PART II#
#########

#inp = [[y.strip() for y in x.strip().split() if y.strip().isdigit()] for x in test.split("\n")]
inp = [[y.strip() for y in x.strip().split() if y.strip().isdigit()] for x in open('inputdata_day6')]
racetime = int(''.join(inp[0]))
record = int(''.join(inp[1]))
win = 0
for x in range(racetime+1):
    result = x*(racetime-x)
    if result > record:
        win += 1

print(win)