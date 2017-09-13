#!/usr/bin/python3

from sys import stdin
from itertools import repeat
def main():
    decks=[]
    maxLength=False
    modulus=10
    div=1
    for line in stdin:
        (index, csv) = line.strip().split(':')
        deck = list(zip(map(int, csv.split(',')), repeat(index)))
        decks += deck

    while not maxLength:
        maxLength = True
        word = ""
        buckets = [list() for _ in range(10)]
        placement = 1
        for card in decks:
            value = card[0]
            least_digit=value % modulus
            least_digit /= div
            buckets[int(least_digit)].append(card)
            if maxLength and least_digit>1:
                maxLength=False

        modulus = modulus * 10
        div = div * 10
        i=0
        for b in range(10):
            bucket = buckets[b]
            for a in bucket:
                decks[i]=a
                i+=1
        placement*=10
    for card in decks:
        word+=card[1]
    # Merge the decks and print result.
    print(word)
if __name__ == "__main__":
    main()
