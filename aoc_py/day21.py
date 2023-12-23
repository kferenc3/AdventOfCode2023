import os
import time
import numpy as np
from collections import deque
start_time = time.time()
os.chdir('/Users/ferenc.kiss/AdventOfCode2023/aoc_rust')

def coords(m):
    lst = []
    for x, y in np.ndenumerate(m):
        lst.append(x)
    return lst

def neighbors(c, h, w):
    c1 = c[0]
    c2 = c[1]
    lst = [(c3, c4) for c3, c4 in [(c1+1, c2), (c1-1, c2), (c1, c2+1), (c1, c2-1)]
           if 0 <= c3 < h and 0 <= c4 < w]
    return lst

test = "...........\n.....###.#.\n.###.##..#.\n..#.#...#..\n....#.#....\n.##..S####.\n.##..#...#.\n.......##..\n.##.#.####.\n.##..##.##.\n..........."
garden = np.asarray([[*x] for x in test.split('\n')])
garden = np.asarray([[*x.replace('\n','')] for x in open('inputdata_day21')])

start = np.where(garden=='S')
start = (start[0][0],start[1][0])
steps = deque([start])
height, width = np.shape(garden)
visited = set()
total_part_i = 0
p = set()

for s in range(1,65):
    for _ in range(len(steps)):
        step = steps.popleft()
        for neighbor in neighbors(step, height, width):
            if neighbor in visited or garden[neighbor] == '#':
                continue
            steps.append(neighbor)
            visited.add(neighbor)
            if s % 2 == 0:
                p.add(neighbor)
                total_part_i +=1

print(total_part_i)

end_time = time.time()
print('Runtime: {:.2}'.format(end_time-start_time))