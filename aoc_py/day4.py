import os
import re
os.chdir('/Users/ferenc.kiss/AdventOfCode2023/aoc_rust')

total_part1 = 0

def common_elements(what, where):
    a = set(what)
    b = set(where)
    if len(a.intersection(b)) > 0:
        return a.intersection(b)
    else:
        return None

test = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53\nCard 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19\nCard 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1\nCard 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83\nCard 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36\nCard 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"
#cards = [x.split(" | ") for x in test.split("\n")]
cards = [x.replace('\n','').split(" | ") for x in open('inputdata_day4')]

cards_won = {}
card_number = 1
for card in cards:
    winning_numbers = [int(x) for x in re.sub(r'Card\s*[0-9]*:','',card[0]).strip().split()]
    my_numbers = [int(x) for x in card[1].split()]
    winners = common_elements(my_numbers,winning_numbers)
    if winners:
        cardpoint = pow(2,len(winners)-1)
        total_part1 += cardpoint
        try: 
            cards_won[card_number] += 1
        except KeyError:
            cards_won[card_number] = 1
        for p in range(cards_won[card_number]):
            i = 1
            for x in range(len(winners)):
                try:
                    cards_won[card_number+i] += 1
                except KeyError:
                    cards_won[card_number+i] = 1
                i += 1
    else:
            try:
                cards_won[card_number] += 1
            except KeyError:
                cards_won[card_number] = 1
    card_number += 1


print(total_part1)
print(sum(cards_won.values()))