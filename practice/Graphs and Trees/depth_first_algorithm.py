def dfs(graph, start):
    visited = []
    stack = [start]

    while stack:
        current = stack.pop()

        if current not in visited:
            visited.append(current)

            for neighbor in range(len(graph[current])):

                if graph[current][neighbor] == 1 and neighbor not in visited:
                    stack.append(neighbor)

    return visited