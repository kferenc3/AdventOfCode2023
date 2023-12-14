import os
import time
import numpy as np
start = time.time()
os.chdir('/Users/ferenc.kiss/AdventOfCode2023/aoc_rust')

def neighbors(c1, c2, h, w):
    lst = [(c3, c4) for c3, c4 in [(c1+1, c2), (c1-1, c2), (c1, c2+1), (c1, c2-1)]
           if 0 <= c3 < h and 0 <= c4 < w]
    return lst

def coords(m):
    lst = []
    for x, y in np.ndenumerate(m):
        lst.append(x)
    return lst

def move_point(point, height, width, direction='north'):
    dirs = {'north': (-1,0), 'south': (1,0), 'east':(0,1), 'west':(0,-1)}
    new_point = tuple(x + y for x, y in zip(point, dirs[direction]))
    if new_point in neighbors(point[0],point[1],height,width):
        return new_point
    else:
        return None

def tilt_platform(points, platform, height, width, dir):
    if dir == 'east':
        zeros = sorted(points, key=lambda x: x[1] ,reverse=True)
    elif dir == 'south':
        zeros = sorted(points, key=lambda x: x[0] ,reverse=True)
    elif dir == 'west':
        zeros = sorted(points, key=lambda x: x[1])
    else:
        zeros = points
    for point in zeros:
        frm = point
        to = move_point(frm, height, width, dir)
        while True:    
            if to is None or platform[to] in ['#','O']:
                platform[point] = '.'
                platform[frm] = 'O'
                break
            else:
                frm = to
                to = move_point(frm,height,width,dir)
    return platform


test = "O....#....\nO.OO#....#\n.....##...\nOO.#O....O\n.O.....O#.\nO.#..O.#.#\n..O..#O..O\n.......O..\n#....###..\n#OO..#...."
#platform = np.asarray([[*x] for x in test.split('\n')])
platform = np.asarray([[*x.replace('\n','')] for x in open('inputdata_day14')])

(height, width) = np.shape(platform)
points = coords(platform)

zeros = list((x,y) for x,y in zip(list(np.where(platform=='O'))[0],list(np.where(platform=='O'))[1]))
for _ in range(1):
    for direction in ['north']:#, 'west','south', 'east']:
        platform = tilt_platform(zeros,platform,height,width,direction)
        zeros = list((x,y) for x,y in zip(list(np.where(platform=='O'))[0],list(np.where(platform=='O'))[1]))

zeros = list(np.where(platform=='O'))[0]

print(sum(list(y-x for x,y in zip(zeros,[height]*len(zeros)))))

end = time.time()
print('Runtime: {:.2}'.format(end-start))

#Part 1 is fine. In theory it works for part 2 as well, but needs refactoring so it actually finishes as well. Maybe sometimes.