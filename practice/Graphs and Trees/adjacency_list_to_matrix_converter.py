def adjacency_list_to_matrix(adj_list):
    num_nodes = len(adj_list)

    matrix = [[0 for _ in range(num_nodes)] for _ in range(num_nodes)]

    for node, neighbors in adj_list.items():
        for neighbor in neighbors:
            matrix[node][neighbor] = 1  # Set to 1 if there's an edge

    for row in matrix:
        print(row)

    return matrix