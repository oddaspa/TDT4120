#!/usr/bin/python3

from sys import stdin
from itertools import repeat
def main():
    decks=[]
    decksLength=0
    newMerge=[]
    for line in stdin:
        (index, csv) = line.strip().split(':')
        deck = list(zip(map(int, csv.split(',')), repeat(index)))
        decks.append(deck)
        decksLength+=1
    word = ""
    newList=[]
    i=0
    while len(newList)!=decksLength:

        if(i%2==0):
            newList.append(mergingList(decks[i],decks[i+1]))
        else:
            newList.append(decks[i])
        i+=2
    for x in range(0,len(newList)-1):
        word+=newList[x][1]
    # Merge the decks and print result.
    print(word)
if __name__ == "__main__":
    main()

def mergingList(pile1, pile2):
    fList = pile1
    sList = pile2
    if len(fList) < len(sList):
        lshort = len(fList)
    else:
        lshort = len(sList)
    newList = []
    for k in range(0, lshort):
        ashort = False
        bshort = False
        i = 0
        j = 0
        a = fList[k]
        print(a)
        b = sList[k]
        if len(a) < len(b):
            minLength = len(a)
            ashort = True
        elif len(a) > len(b):
            minLength = len(b)
            bshort = True
        for x in range(0, minLength - 1):
            print(a[i])
            if (a[i] < b[j]):
                newList.append(a[i])
                i += 1
            else:
                newList.append(b[j])
                j += 1
        if ashort:
            newList.append(b[minLength::])
        elif bshort:
            newList.append(a[minLength::])
        print(newList)
    return newList