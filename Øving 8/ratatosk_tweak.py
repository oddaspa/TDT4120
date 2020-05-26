#!/usr/bin/python3

from sys import stdin


# uses indexes as the parents and then counts how many step to the root (-1)
def tweak(ratatosk_node):
    current_node = ratatosk_node
    depth = -1
    while current_node != -1:
        current_node = nodes[current_node]
        depth += 1
    return depth


function = stdin.readline().strip()
number_of_nodes = int(stdin.readline())

# allocating the nodes
nodes = [-1] * number_of_nodes

start_node = nodes[int(stdin.readline())]

# the ratatosk node
info = int(stdin.readline())

for line in stdin:
    number = line.split()
    parent_node = int(number.pop(0))
    for child_number in number:
        # changing the child index to the parent index

        nodes[int(child_number)] = parent_node


print(tweak(info))
