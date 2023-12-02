import os
os.chdir('/Users/ferenc.kiss/AdventOfCode2023/aoc_rust')

total_part1 = 0
total_part2 = 0

def color_picker(draw, colors):
    result = colors
    cols = ['red', 'green', 'blue']
    if draw[0] == 'Game':
            draw.pop(0)
            draw.pop(0)
    for c in cols:
        try:
            i = draw.index(c)-1
            cubes = int(draw[i])
            if cubes > result[c]:
                result[c] = cubes
        except ValueError:
            continue
    return result

test ="Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green\nGame 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue\nGame 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red\nGame 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red\nGame 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
#lines = [x for x in test.split('\n')]
lines = [x for x in open('inputdata_day2')]
conditions = {'red':12, 'green':13, 'blue':14}

id = 1
for g in lines:
    game = [x.strip() for x in g.split(';')]    
    colors = {'red': 0, 'green': 0, 'blue': 0}
    possible = True
    for d in game:
        draw = d.replace(',','').split()
        res = color_picker(draw, colors)
    for k,v in conditions.items():
         if colors[k] > conditions[k]:
              possible = False
              break
    if possible:
         total_part1 += id
    total_part2 += (res['red'] * res['green'] * res['blue'])
    id += 1
        
print(total_part1)
print(total_part2)

