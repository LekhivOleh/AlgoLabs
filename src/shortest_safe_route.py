def read_input(input_file):
    input_matrix = []
    with open(input_file, 'r') as file:
        for line in file:
            input_matrix.append(list(map(int, line.split(' '))))
    file.close()
    return input_matrix


def write_output(output_matrix, output_file):
    with open(output_file, 'w') as file:
        file.write(str(output_matrix))
    file.close()


def get_path(previous_vertex, start ):
    path = 0
    current_vertex = start
    while current_vertex is not None:
        path += 1
        current_vertex = previous_vertex[current_vertex]
    return path


def find_the_shortest_safe_route(matrix):
    shortest_route = float("inf")
    for i in range(len(matrix)):
        if matrix[i][0] == 1:
            path_len = bfs((i, 0), matrix)
            if path_len < shortest_route and path_len != -1:
                shortest_route = path_len
    if shortest_route == float("inf"):
        return -1
    return shortest_route - 1


def bfs(start_p, matrix):
    previous_vertex = {start_p: None}
    queue = [start_p]
    visited = set()

    while queue:
        current_vertex = queue.pop(0)
        if current_vertex[1] == len(matrix[0]) - 1:
            return get_path(previous_vertex, current_vertex)
        if current_vertex in visited:
            continue
        visited.add(current_vertex)
        for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_x = current_vertex[0] + x
            new_y = current_vertex[1] + y
            if 0 <= new_x < len(matrix) and 0 <= new_y < len(matrix[0]) and matrix[new_x][new_y] == 1 and (new_x, new_y) not in visited:
                queue.append((new_x, new_y))
                previous_vertex[(new_x, new_y)] = current_vertex
    return -1


def add_zeros_to_neighbours(input_file):
    matrix = read_input(input_file)
    if not matrix:
        return -1
    new_matrix = [row[:] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
                    if 0 <= i + y < len(matrix) and 0 <= j + x < len(matrix[0]):
                        new_matrix[i + y][j + x] = 0
    return new_matrix


def main(input_file, output_file):
    try:
        shortest_route = find_the_shortest_safe_route(add_zeros_to_neighbours(input_file))
    except TypeError:
        shortest_route = -1
    write_output(shortest_route, output_file)
