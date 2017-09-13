#!/usr/bin/python3

from sys import stdin
from itertools import repeat
def main():
    decks=[]
    maxLength = 0
    for line in stdin:
        (index, csv) = line.strip().split(':')
        deck = list(zip(map(int, csv.split(',')), repeat(index)))
        decks.append(deck)
        maxLength += len(deck)
    word = ""
    while maxLength != 0: # while there are cards left
        lowestNumber=10000000000
        for pile in decks:
            # next card in pile if not empty pile
            card=next((item for item in pile if item is not None), None)
            if card != None and (card[0] < lowestNumber):
                lowestNumber = card[0]
                lowestCard=card
                lowestPile = pile
        word+=lowestCard[1]
        maxLength -= 1
        lowestPile[lowestPile.index(lowestCard)]=None

    # Merge the decks and print result.
    print(word)
if __name__ == "__main__":
    main()