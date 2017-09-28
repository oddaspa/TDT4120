#!/usr/bin/python3

from sys import stdin, stderr
import traceback


class Node:
    def __init__(self):
        self.child = {}
        self.posi = []


def bygg(ordliste):
    root = Node()
    current_node = root
    for (word,position) in ordliste:
        current_node = root
        for char in word:
            # steps into node of current char.
            if char in current_node.child:
                current_node = current_node.child[char]
            else:
                new_node = Node()
                current_node.child[char] = new_node
                current_node = new_node
        #checks the if we are at the last character in the word
        current_node.posi.append(position)
    return root

def posisjoner(word, index, node):
    posi_array = []
    end_length = len(word)-1
    if word[index] in node.child:
        current_node = node.child[word[index]]
        if index == end_length:
            posi_array+=(current_node.posi)
        else:
            posi_array+=(posisjoner(word,index+1,current_node))
    elif word[index] == "?":
        for key in node.child:
            if index == end_length:
                posi_array+=(node.child[key].posi)
            else:
                posi_array+=(posisjoner(word,index+1,node.child[key]))
    return posi_array

def main():
    try:
        ord = stdin.readline().split()
        ordliste = []
        pos = 0
        for o in ord:
            ordliste.append((o, pos))
            pos += len(o) + 1
        toppnode = bygg(ordliste)
        for sokeord in stdin:
            sokeord = sokeord.strip()
            print("%s:" % sokeord, end='')
            posi = posisjoner(sokeord, 0, toppnode)
            posi.sort()
            for p in posi:
                print(" %s" % p, end='')
            print()
    except:
        traceback.print_exc(file=stderr)


if __name__ == "__main__":
    main()