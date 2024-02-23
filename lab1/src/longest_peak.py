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


# print(get_longest_peak([1,3,5,4,2,9,3,7]))
# print(get_longest_peak([1,2,3,4,5,6,7,8]))
# print(get_longest_peak([8,7,6,5,4,3,2,1]))##
# print(get_longest_peak([1,2]))
# print(get_longest_peak([1,2,3,2,5,6]))
# print(get_longest_peak([1,3,2,4,5,6,7,4,3,2,8,11,10,9]))
# print(get_longest_peak([1,3,2,4,5,6,7,4,3,2,1,8,11,10,9]))
# print(get_longest_peak([1]))
