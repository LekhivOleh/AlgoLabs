from collections import defaultdict


def read_file(file_name):
    with open(f"../resources/{file_name}", "r") as file:
        lines = file.readlines()
        farms = lines[0].strip().split()
        stores = lines[1].strip().split()
        edges = [line.strip().split() for line in lines[2:]]
    return farms, stores, edges


def create_graph(farms, stores, edges):
    graph = defaultdict(dict)
    for edge in edges:
        start, end, weight = edge
        graph[start][end] = int(weight)
    for farm in farms:
        if farm not in graph:
            graph[farm] = {}
        graph["SOURCE"][farm] = float('inf')
    for store in stores:
        if store not in graph:
            graph[store] = {}
        graph[store]["SINK"] = float('inf')
    return dict(graph)


def find_path(graph, start='SOURCE', end='SINK'):
    stack = [(start, [start])]
    paths = []
    while stack:
        vertex, path = stack.pop()
        neighbours = graph[vertex].keys()
        for neighbour in neighbours:
            if neighbour not in path:
                new_path = path + [neighbour]
                if neighbour == end:
                    paths.append(new_path)
                else:
                    stack.append((neighbour, new_path))
    return paths


def max_flow(graph):
    maximum_flow = 0
    paths = find_path(graph)
    for path in paths:
        min_capacity = float('inf')
        for i in range(len(path) - 1):
            start = path[i]
            end = path[i + 1]
            if graph[start][end] < min_capacity:
                min_capacity = graph[start][end]

        for i in range(len(path) - 1):
            start = path[i]
            end = path[i + 1]
            graph[start][end] -= min_capacity

            if graph[start][end] == 0:
                graph[start][end] = float('inf')

        maximum_flow += min_capacity

    return maximum_flow


def find_max_amount(file_name):
    try:
        farms, stores, edges = read_file(file_name)
    except IndexError:
        return -1
    graph = create_graph(farms, stores, edges)
    return max_flow(graph)
