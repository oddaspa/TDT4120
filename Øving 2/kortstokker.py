#!/usr/bin/python3

from sys import stdin
from itertools import repeat

def merge(decks):
    word = ""
    while decks:
        L = decks[0::2]
        R = decks[1::2]

        lowestPile = decks[0]
        for pile in decks:
            if pile[0][0]<lowestNumber:
                lowestNumber = pile[0][0]
                lowestPile=pile
        word+=lowestPile[0][1]
        if len(lowestPile)>1:
            del lowestPile[0]
        else:
            decks.remove(lowestPile)
    return word






def main():
    # Read input.
    decks = []
    for line in stdin:
        (index, csv) = line.strip().split(':')
        deck = list(zip(map(int, csv.split(',')), repeat(index)))
        decks.append(deck)
    # Merge the decks and print result.
    print(merge(decks))


if __name__ == "__main__":
    main()