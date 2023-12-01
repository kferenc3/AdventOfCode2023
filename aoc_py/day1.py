import os
os.chdir('/Users/ferenc.kiss/AdventOfCode2023/aoc_rust')

total_part1 = 0
total_part2 = 0

##PART I##

test ="1abc2\npqr3stu8vwx\na1b2c3d4e5f\ntreb7uchet"
#inp = [[*x] for x in test.split("\n")]
inp = [[*x.replace("\n","")] for x in open('inputdata_day1')]
nums =[]

for x in inp:
    n = [i for i in x if not i.isalpha()]
    val = n[0] + n[-1]
    total_part1 += int(val)
print(total_part1)

##PART II##
test = "two1nine\neightwothree\nabcone2threexyz\nxtwone3four\n4nineeightseven2\nzoneight234\n7pqrstsixteen"
translate = [("one", "o1e"),("two", "t2o"), ("three", "t3e"), ("four", "f4r"),("five", "f5e"),("six", "s6x"),("seven", "s7n"),("eight", "e8t"),("nine", "n9e")]

#inp = [x for x in test.split("\n")]
inp = [x.replace("\n","") for x in open('inputdata_day1')]

for x in range(len(inp)):
    for pattern in translate:
        inp[x] = inp[x].replace(*pattern)

for x in inp:
    n = [i for i in x if i.isnumeric()]
    val = n[0] + n[-1]
    total_part2 += int(val)

print(total_part2)

