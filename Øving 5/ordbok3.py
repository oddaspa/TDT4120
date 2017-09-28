#!/usr/bin/python3

from sys import stdin, stderr
import traceback
class Node:
    def __init__(self):
        self.child = {}
        self.posi = []


def posisjoner(word, index, node):
    posi_array = []
    end_index = len(word)-1
    if word[index] in node.child:
        current_node = node.child[word[index]]
        if index == end_index:
            posi_array+=(current_node.posi)
        else:
            posi_array+=(posisjoner(word,index+1,current_node))
    else:
        for key in node.child:
            if index == end_index:
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
        root = Node()
        for (word, position) in ordliste:
            current_node = root
            for char in word:
                # steps into node of current char
                if char in current_node.child:
                    current_node = current_node.child[char]
                else:
                    current_node.child[char] = Node()
                    current_node = current_node.child[char]
            # checks the if we are at the last character in the word
            current_node.posi.append(position)

        for sokeord in stdin:
            sokeord = sokeord.strip()
            print("%s:" % sokeord, end='')
            posi = posisjoner(sokeord, 0, root)
            posi.sort()
            for p in posi:
                print(" %s" % p, end='')
            print()

    except:
        traceback.print_exc(file=stderr)


if __name__ == "__main__":
    main()