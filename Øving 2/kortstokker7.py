#!/usr/bin/python3

from sys import stdin
from itertools import repeat


def merge_sort(decks):
    result = split(decks)
    result_str = ""
    for tup in result:
        result_str += tup[1]

    return result_str

#Splitter listen rekursivt
def split(list):
    if(len(list) < 2):
        return list[0]
    left = split(list[:len(list)//2])
    right = split(list[len(list)//2:])
    return merge(left,right)

#Sammenligner halvdeler, og limer sammen listene
def merge(left,right):
    result = []
    i,j = 0,0
    while i<len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    if i < len(left):
        result += left[i:]
    if j < len(right):
        result += right[j:]

    return result


def main():
    #Read input.
    decks = []
    for line in stdin:
       (index, csv) = line.strip().split(':')
       deck = list(zip(map(int, csv.split(',')), repeat(index)))
       decks.append(deck)
     #Merge the decks and print result.
    print(merge_sort(decks))

    # liste = [[(1, 'i'), (3, 'i'), (5, 'i'), (8, 'i')], [(2, 'n')], [(4, 't'), (7, 't')], [(6, 'a')], [(9, 'v')]]
    # print(merge_sort(liste))
    # #print(test(liste))


main()

#if __name__ == "__main__":
    #main()