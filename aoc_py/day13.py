import os
import numpy as np
import time
start = time.time()
os.chdir('/Users/ferenc.kiss/AdventOfCode2023/aoc_rust')
test = "#.##..##.\n..#.##.#.\n##......#\n##......#\n..#.##.#.\n..##..##.\n#.#.##.#.\n\n#...##..#\n#....#..#\n..##..###\n#####.##.\n#####.##.\n..##..###\n#....#..#"
test2 = "#.#.#.#.#\n###.#.#.#\n.##.#####\n.##.#####\n###.#.#.#\n#.#.#.#.#\n.#.##.#.#\n#.#..#..#\n..###.#..\n#..#.#.#.\n##.#...#."
#inp = test.split('\n')
inp = [x for x in open('inputdata_day13')]
def transpose_block(lst):
    l=[]
    for i in list(map(list, zip(*lst))):
        l.append(''.join(i))
    return l
    
blocks = []
b = []
for line in [x.replace('\n','') for x in inp]:
    if line == '':
        blocks.append(b)    
        b=[]
    else:
        b.append(line)
blocks.append(b)

total_part_i = 0
for block in blocks:
    #row level reflection
    for i in range(len(block)):
        if block[i-1:i]==block[i:i+1]:
            if i == len(block)//2:
                side1 = block[:i]
                side2 = block[i:]
            elif i < len(block)//2:
                side1 = block[:i]
                side2 = block[i:i+i]
            else:
                side1 = block[i:]
                side2 = block[i-len(side1):i]
            side2.reverse()
            if side1 == side2:
                total_part_i += len(block[:i])*100
    
        #column level reflection:
        block_t = transpose_block(block)
        if block_t[i-1:i]==block_t[i:i+1]:
                if i == len(block_t)//2:
                    side1 = block_t[:i]
                    side2 = block_t[i:]
                elif i < len(block_t)//2:
                    side1 = block_t[:i]
                    side2 = block_t[i:i+i]
                else:
                    side1 = block_t[i:]
                    side2 = block_t[i-len(side1):i]
                side2.reverse()
                if side1 == side2:
                    total_part_i += len(block_t[:i])
                

print(total_part_i)

##After many attempts this is what I could put together by the end of the day. Giving this up for now. 
# My result is still off and not sure where