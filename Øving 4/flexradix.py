#!/usr/bin/python3

from sys import stdin
from string import ascii_lowercase as chars
from random import randint, choice
from operator import itemgetter
from collections import defaultdict

import string
d = dict.fromkeys(string.ascii_lowercase, 0)

def flexradix(A, d):
    for word in A:
        place_word_in_dict(word)



    return True

    # Du må mest sannsynlig lage egne hjelpefunksjoner for denne funksjonen for å løse oppgaven.
    # Funksjonen skal returnere listen A sortert.
    # SKRIV DIN KODE HER
def place_word_in_dict(word):
    d[word[0]].append(word)
def get_character_value(word, index):
    return ord(word[index])

# helper to find the lowest(first) word
def string_compare(word1, word2):
    if word1 < word2:
        length = len(word1)
        i = True
    elif word2 < word1:
        length = len(word2)
        i = False
    else:
        length = len(word1)
    for x in range(length):
        if word1[x] < word1[x]:
            return word1
        elif word2[x] < word2[x]:
            return word2
    # if word1 is shortest return it
    if i:
        return word1
    return word2



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