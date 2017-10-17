#!/usr/bin/python3

from sys import stdin
#import queue

class Node:
    def __init__(self):
        self.child = []
        self.ratatosk = False
        self.next_child = 0
        self.depth = 0
        self.parent = None


def dfs(root):
    node_stack = []
    node_stack.append(root)
    ratatosk = True
    while ratatosk:
        # add depth to children
        current_node = node_stack.pop()

        # try to append children
        if current_node.ratatosk:
            return current_node.depth

        for child in current_node.child:
            child.depth = current_node.depth + 1
        # add children to stack
        node_stack += current_node.child
        # incase of no children just pop

def tweak(ratatosk_node):
    current_node = ratatosk_node
    depth = 0
    while current_node.parent:
        depth += 1
        current_node = current_node.parent
    return depth


def bfs(root):
    node_queue = queue.Queue()
    node_queue.put(root)
    ratatosk = True
    while ratatosk:
        # add depth to children
        current_node = node_queue.get()

        # try to append children
        if current_node.ratatosk:
            return current_node.depth

        # add children and depth
        for child in current_node.child:
            child.depth = current_node.depth + 1
            node_queue.put(child)

function = stdin.readline().strip()
number_of_nodes = int(stdin.readline())
nodes = []
for i in range(number_of_nodes):
    nodes.append(Node())
start_node = nodes[int(stdin.readline())]
info = int(stdin.readline())
ratatosk_node = nodes[info]
ratatosk_node.ratatosk = True
for line in stdin:
    number = line.split()
    temp_node = nodes[int(number.pop(0))]
    for child_number in number:
        child_node = nodes[int(child_number)]
        temp_node.child.append(child_node)
        child_node.parent = temp_node


print(tweak(ratatosk_node))
