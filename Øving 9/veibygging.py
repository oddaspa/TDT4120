from sys import stdin
#stdin = open("input.txt")

Inf = float(1e3000)

def mst(nm):
    # edge case
    if len(nm) == 1:
        smallest_edges = nm

    # Initialize first step
    # array to keep track of weights of the edges we choose to keep
    smallest_edges = []

    # append first node to visited list
    visited_list = [0]
    # while we still have unvisited nodes
    while not len(visited_list) == len(nm):
        # set minimum weight to Inf for each iteration
        min_weight = Inf
        # lets find the smallest edge
        for nodes in visited_list:

        # we scan through all nodes that we already visited
            for neighbour_node,edge_weight in nm[nodes]:
                # go through all edges in a visited node
                    #  if this edge is smaller that the ones we have checked out and the destination is not in visited
                if edge_weight < min_weight and not neighbour_node in visited_list:
                    min_weight = edge_weight
                    next_node = neighbour_node
            # we append the min node with the corresponding min edge
        visited_list.append(next_node)
        smallest_edges.append(min_weight)

    return max(smallest_edges)


lines = []
for str in stdin:
    lines.append(str)
n = len(lines)
neighbour_matrix = [[] for x in range(n)]
node = 0
for line in lines:
    for k in line.split():
        data = k.split(':')
        neighbour = int(data[0])
        weight = int(data[1])
        neighbour_matrix[node].append((neighbour,weight))
    node += 1
print(mst(neighbour_matrix))