# Find the campus route with the fewest connections.
# Practice: graphs, dictionaries, sets, queues, and breadth-first search.
from collections import deque


CAMPUS_MAP = {
    "gate": ["library", "parking"],
    "library": ["gate", "lab", "cafe"],
    "parking": ["gate", "gym"],
    "lab": ["library", "hostel"],
    "cafe": ["library", "hostel"],
    "gym": ["parking", "hostel"],
    "hostel": ["lab", "cafe", "gym"],
}


def find_shortest_route(graph, start, destination):
    if start not in graph or destination not in graph:
        return []

    queue = deque([[start]])
    visited = {start}
    while queue:
        path = queue.popleft()
        current = path[-1]
        if current == destination:
            return path

        # Explore each location once, in breadth-first order.
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])
    return []


def main():
    print("Campus Route Planner")
    print(f"Locations: {', '.join(sorted(CAMPUS_MAP))}")

    while True:
        start = input("Start location (q to quit): ").strip().lower()
        if start == "q":
            break
        if start not in CAMPUS_MAP:
            print("Start location not found.")
            continue

        destination = input("Destination (q to quit): ").strip().lower()
        if destination == "q":
            break
        if destination not in CAMPUS_MAP:
            print("Destination not found.")
            continue

        path = find_shortest_route(CAMPUS_MAP, start, destination)
        if path:
            print(f"Route: {' -> '.join(path)}")
            print(f"Connections: {len(path) - 1}")
        else:
            print("No route connects these locations.")


if __name__ == "__main__":
    main()
