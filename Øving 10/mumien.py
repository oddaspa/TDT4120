from sys import stdin


def best_path(nm, prob):
    path_list = len(nm) * [-1]
    path_list[0] = prob[0]
    visited_nodes = [0]
    current_node = nm[0]
    key = 0
    output = "0"
    while len(visited_nodes) != len(nm):
        max_node = False
        for x in range(len(current_node)):
            if current_node[x]:
                if x not in visited_nodes:
                    if (
                        path_list[nm.index(current_node)] * prob[x] > path_list[x]
                        or path_list[x] == -1
                    ):
                        path_list[x] = path_list[key] * prob[x]
        max_prob = -1
        if len(visited_nodes) == len(nm):
            return visited_nodes
        while not max_node:
            i = 0
            for y in path_list:
                if i not in visited_nodes:
                    if y > max_prob:
                        max_prob = y
                        key = i
                i += 1
            max_node = True

        current_node = nm[key]
        visited_nodes.append(key)
        output += "-" + str(key)
        if (len(nm) - 1) in visited_nodes:
            return output
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
print(best_path(neighbour_matrix, probabilities))
