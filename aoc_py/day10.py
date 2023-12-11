import os
import numpy as np
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

directions = {
    (-1,0): {
        'L':['7','F','|'], 
        'J':['7','F','|'],
        '|':['7','F','|'],
        'F':[],
        '7':[],
        '-':[]},
    (1,0):{
        'L':[], 
        'J':[],
        '|':['L','J', '|'],
        'F':['L','J','|'],
        '7':['L','J','|'],
        '-':[]},
    (0,-1):{
        'L':[], 
        'J':['L','F','-'],
        '|':[],
        'F':[],
        '7':['L','F','-'],
        '-':['L','F','-']},
    (0,1):{
        'L':['J','7','-'], 
        'J':[],'|':[],
        'F':['J','7','-'],
        '7':[],
        '-':['J','7','-']}}

test = "FF7FSF7F7F7F7F7F---7\nL|LJ||||||||||||F--J\nFL-7LJLJ||||||LJL-77\nF--JF--7||LJLJ7F7FJ-\nL---JF-JLJ.||-FJLJJ7\n|F|F-JF---7F7-L7L|7|\n|FFJF7L7F-JF7|JL---7\n7-L-JL7||F7|L7F-7F7|\nL.L7LFJ|||||FJL7||LJ\nL7JLJL-JLJLJL--JLJ.L"
pipemap = np.asarray([[*x] for x in test.split('\n')])
#pipemap = np.asarray([[*x.replace('\n','')] for x in open('inputdata_day10')])
start = (np.where(pipemap=='S')[0][0],np.where(pipemap=='S')[1][0])
(height, width) = np.shape(pipemap)
points = np.full_like(pipemap,0,int)
coordinates = coords(pipemap)
coordinates.remove(start)
to_visit = []
to_visit.append(start)
while to_visit:
    start = to_visit.pop(0)
    neighbor = neighbors(start[0], start[1], height,width)
    check = pipemap[start]
    if check == 'S':
        valid = []
        for v in neighbor:
            n_char = pipemap[v]
            dir = (v[0]-start[0], v[1]-start[1])
            if n_char!='' and n_char!='.':
                if n_char == '|':
                    if dir != (0,1) and dir != (0,-1):
                        valid.append(dir)
                elif n_char == '-':
                    if dir!=(1,0) and dir != (-1,0):
                        valid.append(dir)
                elif n_char == 'F':
                    if dir!=(0,1) and dir != (1,0):
                        valid.append(dir)
                else:
                    valid.append(dir)
        match valid:
            case [(1,0),(0,-1)]: check = '7'
            case [(1,0),(0,1)]: check = 'F'
            case _: print('oops')
    for v in neighbor:
        dir = (v[0]-start[0], v[1]-start[1])
        if pipemap[v] in directions[dir][check]:
            if points[v] == 0:
                points[v] += points[start] + 1
                to_visit.append(v)
print(np.max(points))