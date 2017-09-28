#!/usr/bin/python3

from sys import stdin
from string import ascii_lowercase as chars
from random import randint, choice
from operator import itemgetter
from collections import defaultdict

def flexradix(A, d):
    tmp_list = []
    for word1 in A:
        if tmp_list == []:
            tmp_list.append(word1)
        else:
            i = 0
            for word2 in tmp_list:
                print(word2)
                print(tmp_list)
                if word1 < word2:
                    tmp_list.insert(i,word1)
                    break
                elif i == len(tmp_list):
                    tmp_list.append(word1)
                i += 1
    return tmp_list




def main():
    d = int(stdin.readline())
    strings = []
    for line in stdin:
        strings.append(line.rstrip())
    A = flexradix(strings, d)
    for string in A:
        print(string)


if __name__ == "__main__":
    main()