import os
import time
import numpy as np
start = time.time()
os.chdir('/Users/ferenc.kiss/AdventOfCode2023/aoc_rust')
#sequences = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7".split(',')
sequences = [x.replace('\n','').split(',') for x in open('inputdata_day15')][0]

def sequence_hash(seq):
    result = 0
    for char in seq:
        result = ((result+ord(char))*17)%256
    return result

boxes = [[] for _ in range(256)]
part_i_total = 0
part_ii_total = 0

for sequence in sequences:
    part_i_total += sequence_hash(sequence)
    if sequence.__contains__('='):
        label, focal_length = sequence.split('=')
        box = sequence_hash(label)
        boxlabels = [x[0] for x in boxes[box]]
        if label in boxlabels:
            boxes[box][[i for i,x in enumerate(boxes[box]) if x[0]==label][0]][1] = int(focal_length)
        else:
            boxes[box].append([label, int(focal_length)])
    elif sequence.__contains__('-'):
        label = sequence[:-1]
        box = sequence_hash(label)
        if label in [x[0] for x in boxes[box]]:
            boxes[box].pop([i for i,x in enumerate(boxes[box]) if x[0]==label][0])
        else:
            pass
        
vals = [(i+1,[(j+1,z[1]) for j,z in enumerate(x)]) for i,x in enumerate(boxes) if x != []]
for box in vals:
    for lens in box[1]:
        part_ii_total += box[0] * lens[0] *lens[1]

print(part_i_total)
print(part_ii_total)
end = time.time()
print('Runtime: {:.2}'.format(end-start))