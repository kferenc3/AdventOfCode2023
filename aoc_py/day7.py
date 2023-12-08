import os
from collections import Counter
os.chdir('/Users/ferenc.kiss/AdventOfCode2023/aoc_rust')


test = "32T3K 765\nT55J5 684\nKK677 28\nKTJJT 220\nQQQJA 483"
#inp = [[y for y in x.split()] for x in test.split("\n")]
inp = [[y for y in x.split()] for x in open('inputdata_day7')]

cards = 'AKQJT98765432'
cards2 = 'AKQT98765432J'
handtype = {'fives': 1, 'fours': 2, 'full': 3, 'threes': 4, 'twopair': 5, 'onepair': 6, 'high': 7}


def solver(i,joker=False):
    hands = []
    ranks = []
    strength =[]
    bids = []

    if joker:
        cards = 'AKQT98765432J'    
    else:    
        cards = 'AKQJT98765432'
    
    for pair in i:
        pairs = [x for x in pair]
        hand = pair[0]
        bids.append(int(pair[1]))
        ranks.append([cards.index(x) for x in hand])
        cntr = Counter(hand)
        if joker:
            if 'J' in hand and hand != 'JJJJJ':
                if cntr.most_common()[0][0] != 'J':
                    hand = hand.replace('J', cntr.most_common()[0][0])
                else:
                    hand = hand.replace('J', cntr.most_common()[1][0])
                cntr = Counter(hand)
        hands.append(hand)
        match sorted(cntr.values()):
            case [5]: strength.append(1)
            case [1,4]: strength.append(2)
            case [2,3]: strength.append(3)
            case [1,1,3]: strength.append(4)
            case [1,2,2]: strength.append(5)
            case [1,1,1,2]: strength.append(6)
            case _: strength.append(7)
    
    bids = sorted(bids, key= lambda l: (strength[bids.index(l)],ranks[bids.index(l)]))
    bids.reverse()
    result = 0
    for i, b in enumerate(bids):
        result += (i+1) * b
    return result


print('Part I: ', solver(inp,False))
print('Part II:', solver(inp,True))