import os
os.chdir('/Users/ferenc.kiss/AdventOfCode2023/aoc_rust')

test = "0 3 6 9 12 15\n1 3 6 10 15 21\n10 13 16 21 30 45"
#oasis = [[int(y) for y in x.split(' ')] for x in test.split("\n")]
oasis = [[int(y) for y in x.split(' ')] for x in open('inputdata_day9')]

def pattern_extractor(lst):
    res = []
    for id in range(len(lst)):
        if id <= len(lst)-2:
            res.append(lst[id+1]-lst[id])
    return res

forecast = []
history = []
total_part_i = 0
total_part_ii = 0

for line in oasis:
    forecast.append(line)
    while set(pattern_extractor(forecast[-1])) != {0}:
        forecast.append(pattern_extractor(forecast[-1]))
    forecast.reverse()
    history = forecast.copy()
    for fc in range(len(forecast)):
        if fc <= len(forecast)-2:
            forecast[fc+1].append(forecast[fc][-1]+forecast[fc+1][-1])
    for h in range(len(history)):
        if h <= len(history)-2:
            history[h+1].insert(0, history[h+1][0]- history[h][0])

    total_part_i += forecast[-1][-1]
    total_part_ii += history[-1][0]
    forecast.clear()

print(total_part_i)
print(total_part_ii)