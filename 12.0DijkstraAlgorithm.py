import heapq

def dijkstra(graph, start):
    """
    Dijkstra's algorithm for finding the shortest paths from a single source.
    :param graph: Dictionary where keys are nodes and values are lists of (neighbor, weight) pairs.
    :param start: The starting node.
    :return: Dictionary with shortest distances from the start node to all other nodes.
    """
    # Priority queue to store (distance, node)
    priority_queue = []
    # Dictionary to store the shortest distance to each node
    shortest_distances = {node: float('inf') for node in graph}
    shortest_distances[start] = 0

    # Push the starting node into the priority queue
    heapq.heappush(priority_queue, (0, start))

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # If the current distance is greater than the recorded shortest distance, skip
        if current_distance > shortest_distances[current_node]:
            continue

        # Explore neighbors
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # If a shorter path is found
            if distance < shortest_distances[neighbor]:
                shortest_distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return shortest_distances


# Example Usage
if __name__ == "__main__":
    # Example graph represented as an adjacency list
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 6)],
        'C': [('A', 4), ('B', 2), ('D', 3)],
        'D': [('B', 6), ('C', 3)]
    }

    start_node = 'A'
    shortest_paths = dijkstra(graph, start_node)

    print(f"Shortest distances from node {start_node}:")
    for node, distance in shortest_paths.items():
        print(f"Node {node}: {distance}")
