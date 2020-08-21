arr = [7, 4, 6, -2, 1]


def bubble_sort(arr: list):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(arr)


bubble_sort(arr)
