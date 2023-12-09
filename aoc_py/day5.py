import os
os.chdir('/Users/ferenc.kiss/AdventOfCode2023/aoc_rust')

test = "seeds: 79 14 55 13\n\nseed-to-soil map:\n50 98 2\n52 50 48\n\nsoil-to-fertilizer map:\n0 15 37\n37 52 2\n39 0 15\n\nfertilizer-to-water map:\n49 53 8\n0 11 42\n42 0 7\n57 7 4\n\nwater-to-light map:\n88 18 7\n18 25 70\n\nlight-to-temperature map:\n45 77 23\n81 45 19\n68 64 13\n\ntemperature-to-humidity map:\n0 69 1\n1 0 69\n\nhumidity-to-location map:\n60 56 37\n56 93 4"
#inp = [x for x in test.split('\n')]
inp = [x.replace('\n','') for x in open('inputdata_day5')]

########
#PART I#
########
seeds = [int(x) for x in inp[0].lstrip('seds: ').split(' ')]

location =[]
for start in seeds:
    seed = start
    found = False
    for line in inp[3:]:
        if line and line[0].isdigit():
            (source, destination, length) = (int(x) for x in line.split())
            if not found:
                if seed >= destination and seed <= destination+(length-1):
                    seed = source + (seed - destination)
                    found = True
            else:
                continue
        elif line and line[0].isalpha:
            found = False
        else:
            continue
        
    location.append(seed)
            
print('Part I:'+'\t', min(location))

#########
#PART II#
#########

seeds = [int(x) for x in inp[0].lstrip('seds: ').split(' ')]
seedranges = []
for i in range(0, len(seeds)-2+1, 2):
    seed = seeds[i:i+2]
    seedranges.append((seed[0],seed[0]+seed[1]-1))


sections = []
section = []
for line in inp[3:]:
    if not line:
        continue
    if line[0].isdigit():
        (source, destination, length) = (int(x) for x in line.split())
        section.append((source, destination, length))
    elif line[0].isalpha():
        sections.append(section)
        section = []

for i, section in enumerate(sections):
    temp = []
    while seedranges:
    ##while loop on the seedranges
    ##once the range is empty  start new section and copy temp to seed
        rng = seedranges.pop()
        processed = False
        for map in section:
            source = map[0]
            frm = map[1]
            to = map[1]+ map[2]-1
            ##full overlap:
            if rng[0] >= frm <= rng[1] <= to:
                f = source + (rng[0]-frm)
                t = source + (rng[0]-frm) +(rng[1]-rng[0])
                processed = True
                temp.append((f,t))
            ##upper overlap
            elif rng[0] >= frm & rng[0] >= to & rng[1]> to:
                f = source + (rng[0]-frm)
                t = source + (rng[0]-frm) + (to - rng[0])
                processed = True
                temp.append((f,t))
                seedranges.append((to+1, rng[1]))
            ##lower
            elif rng[0] < frm <= rng[1] <= to:
                f = source
                t = source + (rng[1] - frm)
                processed = True
                temp.append((f,t))
                seedranges.append((rng[0], frm-1))
            #middle
            elif rng[0] < frm & rng[1] > to:
                f = source
                t = source + (to - frm)
                processed = True
                temp.append((f,t))
                seedranges.append((rng[0], frm-1))
                seedranges.append((to+1, rng[1]))
            ##no overlap
            else:
                continue
        if not processed:
            temp.append(rng)        
    seedranges = temp.copy()
    temp.clear()

lows = []
for s in seedranges:
    lows.append(s[0])

print('Part II:', min(lows))