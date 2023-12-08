import os
import math
os.chdir('/Users/ferenc.kiss/AdventOfCode2023/aoc_rust')

test = "LLR\n\nAAA = (BBB, BBB)\nBBB = (AAA, ZZZ)\nZZZ = (ZZZ, ZZZ)"
test2 = "LR\n\n11A = (11B, XXX)\n11B = (XXX, 11Z)\n11Z = (11B, XXX)\n22A = (22B, XXX)\n22B = (22C, 22C)\n22C = (22Z, 22Z)\n22Z = (22B, 22B)\nXXX = (XXX, XXX)"
#inp = [x for x in test.split("\n") if x != '']
#inp = [x for x in test2.split("\n") if x != '']
inp = [x.replace('\n', '') for x in open('inputdata_day8') if x != '\n']

directions = [int(y.replace('L','0').replace('R','1')) for y in inp[0]]

nodes = {}

for x in inp[1:]:
    nodes[x.split(' = ')[0]] = x.split(' = ')[1].replace('(','').replace(')','').split(', ')

#PART I
node = 'AAA'
step = 0       
while node != 'ZZZ':
    for d in directions:
        node = nodes[node][d]
        step += 1
print('Part I: ', step)

#PART II
steps = []
starters = [x for x in list(nodes.keys()) if x[-1] == 'A']
for s in starters:
    node = s
    step = 0
    while node[-1] != 'Z':
        for d in directions:
            node = nodes[node][d]
            step += 1
    steps.append(step)
print('Part II:', math.lcm(*steps))