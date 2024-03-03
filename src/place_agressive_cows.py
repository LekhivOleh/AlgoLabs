def distance_between_cows(n, c, free_sections):
    result = 0
    free_sections.sort()
    prev_elem = free_sections[0]

    if c == 2:
        return free_sections[n - 1] - free_sections[0]

    avg_placement = (free_sections[n - 1] - free_sections[0]) / (c - 1)

    for i in range(1, c):
        closest_elem = find_closest_elem(free_sections, len(free_sections), free_sections[0] + avg_placement * i)

        if result == 0 or abs(closest_elem - prev_elem) < result:
            result = abs(closest_elem - prev_elem)
        prev_elem = closest_elem

    return result


def find_closest_elem(arr, n, target):
    left, right = 0, n - 1
    while left < right:
        if abs(arr[left] - target) <= abs(arr[right] - target):
            right -= 1
        else:
            left += 1
    return arr[left]
