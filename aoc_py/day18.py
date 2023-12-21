##The source of the area function is: https://arachnoid.com/area_irregular_polygon/index.html
## Totally not an ideal solution for part 2, but it did run in a couple of minutes so I didn't bother changing anything
import os
import time
import numpy as np
start_time = time.time()
os.chdir('/Users/ferenc.kiss/AdventOfCode2023/aoc_rust')

def find_area_perim(array):
    a = 0
    p = 0
    ox,oy = array[0]
    for x,y in array[1:]:
        a += (x*oy-y*ox)
        p += abs((x-ox)+(y-oy)*1j)
        ox,oy = x,y
    return a/2,p


#test = "R 6 (#70c710)\nD 5 (#0dc571)\nL 2 (#5713f0)\nD 2 (#d2c081)\nR 2 (#59c680)\nD 2 (#411b91)\nL 5 (#8ceee2)\nU 2 (#caa173)\nL 1 (#1b58a2)\nU 2 (#caa171)\nR 2 (#7807d2)\nU 3 (#a77fa3)\nL 2 (#015232)\nU 2 (#7a21e3)"
#inp = [x.split(' ') for x in test.split('\n')]
inp = [x.replace('\n','').split(' ') for x in open('inputdata_day18')]
start = (0,0)
trench = []
trench2 = []
trench.append(start)
trench2.append(start)
directions = {
    'R': (0,1),
    'L': (0,-1),
    'U': (-1,0),
    'D': (1,0)
}
part2dir = {
    0:'R',
    1:'D',
    2:'L',
    3:'U'
}
c = start
c2 = start
for inst in inp:
    p2 = inst[2].replace('(','').replace(')','')
    step2 = int(p2[1:-1],16)
    d2 = directions[part2dir[int(p2[-1])]]
    d = directions[inst[0]]
    for i in range(int(inst[1])):
        c = tuple(x + y for x, y in zip(c, d))
        trench.append(c)
    for z in range(step2):
        c2 = tuple(x + y for x, y in zip(c2, d2))
        trench2.append(c2)

##PART I
area, perim = find_area_perim(trench)
print(int(area + perim//2+1))

##PART II
area, perim = find_area_perim(trench2)
print(int(area + perim//2+1))

end_time = time.time()
print('Runtime: {:.2}'.format(end_time-start_time))