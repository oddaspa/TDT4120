#!/usr/bin/python3

from sys import stdin
from itertools import repeat

def merge(decks):
    word = ""
    maxElements=0
    counter=0
    RADIX = 10
    placement=1
    for pile in decks:
        maxElements+=len(pile)
    # declare and initialize buckets
    buckets = [list() for _ in range(RADIX)]
    while counter != maxElements:
        for pile in decks:
            buck[pile[0][0]%placement].append(pile)

        counter+=1
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