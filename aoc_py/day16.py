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

def beambounce(symbol,h, w, coord,dir):
    direction = {'up':(-1,0),'down':(1,0),'left':(0,-1),'right':(0,1)}
    res = []
    if symbol == '.':
        l = [[tuple(x+y for x,y in zip(coord,direction[dir])), dir]]
    elif dir in ['left', 'right'] and symbol == '-':
        l = [[tuple(x+y for x,y in zip(coord,direction[dir])), dir]]
    elif dir in ['up', 'down'] and symbol == '|':
        l = [[tuple(x+y for x,y in zip(coord,direction[dir])), dir]]
    elif (dir == 'right' and symbol == 'U') or (dir == 'left' and symbol == 'D'):
        l = [[tuple(x+y for x,y in zip(coord,direction['up'])), 'up']]
    elif (dir == 'right' and symbol == 'D') or (dir == 'left' and symbol == 'U'):
        l = [[tuple(x+y for x,y in zip(coord,direction['down'])), 'down']]
    elif dir in ['right', 'left'] and symbol == '|':
        l = [[tuple(x+y for x,y in zip(coord,direction['down'])), 'down'],[tuple(x+y for x,y in zip(coord,direction['up'])), 'up']]
    elif dir in ['up', 'down'] and symbol == '-':
        l = [[tuple(x+y for x,y in zip(coord,direction['left'])), 'left'],[tuple(x+y for x,y in zip(coord,direction['right'])), 'right']]
    elif (dir == 'up' and symbol == 'D') or (dir == 'down' and symbol == 'U'):
        l = [[tuple(x+y for x,y in zip(coord,direction['left'])), 'left']]
    elif (dir == 'up' and symbol == 'U') or (dir == 'down' and symbol == 'D'):
        l = [[tuple(x+y for x,y in zip(coord,direction['right'])), 'right']]
    
    for x in l:
        if 0>x[0][0] or x[0][0]>=h or 0>x[0][1] or x[0][1]>=w:
            pass
        else:
            res.append(x)
    return res

#test = r'.|...\....\n|.-.\.....\n.....|-...\n........|.\n..........\n.........\\n..../.\\..\n.-.-/..|..\n.|....-|.\\n..//.|....'
#test = test.replace(r'\n', 'n').replace('\\', 'D').replace('/', 'U')
#test = test.replace('n','\n')
inp = r''.join([x for x in open('inputdata_day16')]).replace('\\','D').replace('/', 'U')

beam = [[(0,0), 'right']]


#grid = np.asarray([[*x] for x in test.split('\n')])
grid = np.asarray([[*x] for x in inp.split('\n')])
height, width = np.shape(grid)
energized = np.full_like(grid,'.')

for _ in range (1000000):
    b = beam.pop(0)
    energized[b[0]] = '#'
    symbol = grid[b[0]]
    new_items = beambounce(symbol, height, width, b[0], b[1])
    for ne in new_items:
        if ne not in beam:
            beam.append(ne)

print(len(np.where(energized=='#')[0]))    

end = time.time()
print('Runtime: {:.2}'.format(end-start))

#Dumb brute force method, but it got 1 start. I got bored/fed up with this day, so I'll leave it at that for now.