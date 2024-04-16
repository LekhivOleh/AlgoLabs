def read_file(input_file):
    cities = []
    storages = []
    gas_pipes = []

    with open(input_file, "r", encoding='utf-8') as file:
        lines = file.readlines()
        if lines:
            cities = lines[0].strip().split()  # get all cities form the first line
            storages = lines[1].strip().split()  # get all storages from the second line
            gas_pipes = [line.strip().split() for line in lines[2:]]
    return cities, storages, gas_pipes


def write_file(output_file, result):
    with open(output_file, "w", encoding='utf-8') as file:
        file.writelines(result)


def dfs(graph, start_p):
    stack = [start_p]
    visited = []
    while stack:
        current = stack.pop()
        visited.append(current)
        for neighbour in graph[current]:
            stack.append(neighbour)
    return visited


def check_if_city_is_accessible(storage, visited, cities):
    not_accessible = []
    for city in cities:
        if city not in visited:
            not_accessible.append(city)
    return storage, not_accessible


def check_gas_distribution_between_cities(input_file, output_file):
    cities, storages, gas_pipes = read_file(input_file)

    if len(cities) == 0:
        write_file(output_file, ['-1'])
        return

    inaccessible_cities = []

    graph = {city: [] for city in cities}
    for gas_pipe in gas_pipes:
        source, destination = gas_pipe
        if source in cities and destination in cities:
            graph[source].append(destination)

    for storage in storages:
        if storage not in cities:
            continue
        visited = dfs(graph, storage)
        current_storage = check_if_city_is_accessible(storage, visited, cities)
        if len(current_storage[1]) == 0:
            continue
        inaccessible_cities.append(str(check_if_city_is_accessible(storage, visited, cities)))

    write_file(output_file, inaccessible_cities)
