"""
Napisz skrypt z implementacją algorytmu Dijkstry. Wykorzytaj wiedzę z zajęć.
"""

def dijkstra(graph, start):
    # odległości od startowego wierzchołka
    distances = {}
    for vertex in graph:
        distances[vertex] = float('inf')
    distances[start] = 0

    unvisited_vertices = list(graph.keys())

    while unvisited_vertices:
        current_vertex = None
        for vertex in unvisited_vertices:
            if current_vertex is None or distances[vertex] < distances[current_vertex]:
                current_vertex = vertex

        unvisited_vertices.remove(current_vertex)

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance

    return distances


graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 1, 'D': 4},
    'C': {'A': 3, 'B': 1, 'D': 1},
    'D': {'B': 4, 'C': 1}
}

shortest_paths = dijkstra(graph, 'A')

for vertex in shortest_paths:
    print(f"Najkrótsza ścieżka do wierzchołka {vertex}: {shortest_paths[vertex]}")
