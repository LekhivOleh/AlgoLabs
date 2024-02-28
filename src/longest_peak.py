def get_longest_peak(arr):
    result = 0
    left_len = 0
    right_len = 0
    for i in range(len(arr) - 1):
        if arr[i] < arr[i + 1]:
            if right_len == 0:
                left_len += 1
            else:
                right_len = 0
                left_len = 1
        if arr[i] > arr[i + 1]:
            right_len += 1
            if left_len != 0:
                if result <= right_len + left_len + 1:
                    result = left_len + right_len + 1
    return result


