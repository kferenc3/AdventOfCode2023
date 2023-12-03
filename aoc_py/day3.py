import numpy as np
import os
os.chdir('/Users/ferenc.kiss/AdventOfCode2023/aoc_rust')

total_part1 = 0
total_part2 = 0

def coords(m):
    lst = []
    for x, y in np.ndenumerate(m):
        lst.append(x)
    return lst

def neighbors(c1, c2, h, w):
    lst = [(c3, c4) for c3, c4 in [(c1+1, c2), (c1-1, c2), (c1, c2+1), (c1, c2-1), (c1+1,c2+1), (c1-1,c2-1), (c1-1, c2+1), (c1+1, c2-1)]
           if 0 <= c3 < h and 0 <= c4 < w]
    return lst

def common_elements(what, where):
    a = set(what)
    b = set(where)
    if len(a.intersection(b)) > 0:
        return a.intersection(b)
    else:
        return None

test = "467..114..\n...*......\n..35..633.\n......#...\n617*......\n.....+.58.\n..592.....\n......755.\n...$.*....\n.664.598.."
#inp = [[*x] for x in test.split("\n")]
inp = [[*x.replace("\n",".")] for x in open('inputdata_day3')]

nums = []
symbols = []
asterisks = {}
height = len(inp)
width = len(inp[0])

for c in coords(inp):
    if inp[c[0]][c[1]] != "." and inp[c[0]][c[1]].isnumeric():
        nums.append(c)
    elif inp[c[0]][c[1]] != "." and not inp[c[0]][c[1]].isnumeric():
        symbols.append(c)
        if inp[c[0]][c[1]] == "*":
            asterisks[c] = []

numstr = ''
start = (-1,-1)
coordlist = []
numdict = {}
id = 0
for n in nums:
    if start == (-1,-1):
        start = n
        coordlist.append(n)
        numstr = numstr + inp[n[0]][n[1]]
    elif n[0] == start[0] and n[1] == start[1]+1:
        start = n
        coordlist.append(n)
        numstr = numstr + inp[n[0]][n[1]]
    else:
        numdict[id] = (int(numstr),coordlist)
        id += 1
        coordlist = []
        numstr = ''
        start = n
        coordlist.append(n)
        numstr = numstr + inp[n[0]][n[1]]
numdict[id] = (int(numstr),coordlist)


for k,v in numdict.items():
    to_sum = False
    for i in v[1]:
        if common_elements(neighbors(i[0],i[1],height,width),symbols) is not None:
            to_sum=True
            for a in asterisks.keys():
                if common_elements(neighbors(i[0],i[1],height,width),[a]) is not None:
                    asterisks[a].append(v[0])
            break
    if to_sum:
        total_part1 += v[0]

for k,v in asterisks.items():
    if len(v) == 2:
        total_part2 += np.prod(v)
 
print(total_part1)
print(total_part2)