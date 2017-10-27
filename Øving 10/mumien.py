from sys import stdin, stderr
class Node():
    def __init__(self, prob, neighbours ):
        self.prob = prob
        self.neighbours = neighbours

def best_path(nm, prob):
    path_finished = False
    current_node = nm[0]
    visited_nodes = [0]
    i = 0
    nodes = []
    path_list = len(nm) * [-1]
    path_list[0] = prob[0]
    while not path_finished:
        max_weight = -1
        for x in range(len(current_node)-1):
            index_of_neighbour = x
            print(visited_nodes)
            if prob[index_of_neighbour] > path_list[index_of_neighbour] and not index_of_neighbour in visited_nodes:
                path_list[index_of_neighbour] = prob[index_of_neighbour]*prob[nm.index(current_node)]
                current_node = nm[index_of_neighbour]
                next_index = index_of_neighbour
        for weight in path_list:
            if weight > max_weight and not path_list.index(weight) in visited_nodes:
                max_weight = weight

        next_node = nm[path_list.index(max_weight)]
        visited_nodes.append(next_index)
        print(path_list)
        if len(visited_nodes) == len(nm):
            path_finished = True
    print(path_list)
    return True

n = int(stdin.readline())
probabilities = [float(x) for x in stdin.readline().split()]
neighbour_matrix = []
for line in stdin:
    neighbour_row = [0] * n
    neighbours = [int(neighbour) for neighbour in line.split()]
    for neighbour in neighbours:
        neighbour_row[neighbour] = 1
    neighbour_matrix.append(neighbour_row)
print (best_path(neighbour_matrix, probabilities))