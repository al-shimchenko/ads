graph = {
    "Пекин": {"Дели": 3784, "Токио": 2100, "Сеул": 955},
    "Дели": {"Пекин": 3784, "Джакарта": 5828, "Тегеран": 3369},
    "Токио": {"Пекин": 2100, "Джакарта": 5786, "Бангкок": 4600},
    "Джакарта": {"Дели": 5828, "Токио": 5786, "Бангкок": 1425},
    "Сеул": {"Пекин": 955, "Бангкок": 3687},
    "Бангкок": {"Токио": 4600, "Джакарта": 1425, "Сеул": 3687},
    "Тегеран": {"Дели": 3369}
}

distances = {}
visited = set()


def find_min_distance(graph):
    min_distance = float("inf")
    min_vertex = None
    for vertex in graph:
        if vertex not in visited and distances[vertex] < min_distance:
            min_distance = distances[vertex]
            min_vertex = vertex
    return min_vertex


def dijkstra(graph, start):
    for vertex in graph:
        distances[vertex] = float("inf")
    distances[start] = 0

    while len(visited) < len(graph):
        current_vertex = find_min_distance(graph)
        visited.add(current_vertex)
        for neighbor in graph[current_vertex]:
            if neighbor not in visited:
                distance = distances[current_vertex] + graph[current_vertex][neighbor]
                if distance < distances[neighbor]:
                    distances[neighbor] = distance


dijkstra(graph, "Пекин")

# for vertex in distances:
# print(f"Расстояние от Пекина до {vertex} равно {distances[vertex]} км.")

print(f"Расстояние от Пекина до {'Джакарта'} равно {distances['Джакарта']} км.")
