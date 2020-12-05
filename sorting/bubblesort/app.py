arr = [7, 4, 6, -2, 1]


def bubble_sort(arr: list) -> list:
    n = len(arr)

    for i in range(n - 1):
        current_swaps = 0
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                current_swaps += 1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if current_swaps == 0:
            break
    return arr


print(bubble_sort(arr))
