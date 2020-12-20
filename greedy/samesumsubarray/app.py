from collections.abc import Iterable


def sub_array_with_equal_sum(arr):
    n = len(arr)
    total_left, count = 0, []
    for i in range(0, n):
        total_left += arr[i]  # total_left = [arr[i]+ ... + arr[n]]
        # find the sum of other elements
        # first loop given [0, 4, -1, 0, 3] will be
        # left = [0] right = 4 + (-1) + 0 + 3
        total_right = 0
        for j in range(i + 1, n):
            total_right += arr[j]
        if total_left == total_right:
            # found a sub array where right equals left
            count.append(i + 1)
    return count


def solution(A, B):
    if not isinstance(A, Iterable):
        return 0
    if not isinstance(B, Iterable):
        return 0
    subarray1 = sub_array_with_equal_sum(A)
    subarray2 = sub_array_with_equal_sum(B)
    count = 0
    for i in subarray1:
        if i in subarray2:
            count + 1

    return count


A = [0, 4, -1, 0, 3]
B = [0, -2, 5, 0, 3]
