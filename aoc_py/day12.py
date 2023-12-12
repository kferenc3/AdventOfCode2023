import os
import itertools
import time
start = time.time()
os.chdir('/Users/ferenc.kiss/AdventOfCode2023/aoc_rust')

test = "???.### 1,1,3\n.??..??...?##. 1,1,3\n?#?#?#?#?#?#?#? 1,3,1,6\n????.#...#... 4,1,1\n????.######..#####. 1,6,5\n?###???????? 3,2,1"
test2 = "????.######..#####. 1,6,5"
#inp = (x.split(' ') for x in test2.split('\n'))
inp = (x.replace('\n','').split(' ') for x in open('inputdata_day12'))

def combocounter(inp, part):
    validcombo = 0
    for x in inp:
        if part == 1:
            (springs, instructions) = (x[0], [int(y) for y in x[1].split(',')])
        elif part == 2:
            instructions = [int(z) for z in ''.join([(x[1]+',')*5])[:-1].split(',')]
            springs = ''.join([(x[0]+'?') * 5])[:-1]
        damaged = len([d for d, x in enumerate(springs) if x == '#'])
        total_damaged = sum(instructions)
        remaining = total_damaged-damaged
        unknown = [u for u,x in enumerate(springs) if x == '?']
        for places in itertools.combinations(unknown,remaining):
            ranges = []
            r = 0
            for i, s in enumerate(springs):
                if s == '?':
                    if i in places:
                        r += 1
                    else:
                        if r > 0:
                            ranges.append(r)
                            if ranges != instructions[:len(ranges)]:
                                break
                        r = 0
                else:
                    if s == '#':
                        r += 1
                    else:
                        if r > 0:
                            ranges.append(r)
                            if ranges != instructions[:len(ranges)]:
                                break
                        r = 0
            if r > 0:
                ranges.append(r)
            if ranges == instructions:
                validcombo += 1
            
    return validcombo


print(combocounter(inp,1))
#print(combocounter(inp,2))
end = time.time()
print('Runtime: {:.2}'.format(end-start))

###The code has functionality for part 2 but it will never finish obviously 
# Part 2 is way out of league for my coding knowledge so I'll settle for 1 star today.

