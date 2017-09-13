#!/usr/bin/python3

from sys import stdin
from itertools import repeat
def main():
    decks=[]
    for line in stdin:
        (index, csv) = line.strip().split(':')
        deck = list(zip(map(int, csv.split(',')), repeat(index)))
        decks.append(deck)
    word = ""
    numOfLetters=len(decks)
    usedNumbers=[numOfLetters]
    while decks:
        lowestNumber = decks[0][0][0]
        lowestPile = decks[0]
        for pile in decks:
            if pile[0][0]<lowestNumber:
                 lowestNumber = pile[0][0]
                 lowestPile=pile
        word+=lowestPile[0][1]
        usedPiles.append()
        if len(lowestPile)>1:
            del lowestPile[0]
        else:
            decks.remove(lowestPile)

    # Merge the decks and print result.
    print(word)
if __name__ == "__main__":
    main()