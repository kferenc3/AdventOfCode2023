import os
import numpy as np
os.chdir('/Users/ferenc.kiss/AdventOfCode2023/aoc_rust')

test = "...#......\n.......#..\n#.........\n..........\n......#...\n.#........\n.........#\n..........\n.......#..\n#...#....."
#starmap = np.asarray([[*x] for x in test.split('\n')])
starmap = np.asarray([[*x.replace('\n','')]for x in open('inputdata_day11')])

empty_col = []
empty_row = []
(height, width) = np.shape(starmap)
for i in range(width):
    if set(starmap[:,i]) == {'.'}:
        empty_col.append(i)

for i in range (height):
    if set(starmap[i]) == {'.'}:
        empty_row.append(i)


g = np.where(starmap=='#')
galaxies = []

for i in range(len(g[0])):
    x = g[0][i]
    y = g[1][i]
    for col in empty_col:
        if col < g[1][i]:
            y += 999999
    for row in empty_row:
        if row < g[0][i]:
            x += 999999
    galaxies.append((x,y))

distances = 0
for pairs in [(a,b) for id, a in enumerate(galaxies) for b in galaxies[id + 1:]]:
    distances += abs(pairs[0][0] - pairs[1][0]) + abs(pairs[0][1] - pairs[1][1])

print(distances)

