l = [7, 4, 6, -2, 1]


def insertion_sort(arr: list):
    n = len(arr)
    for i in range(n - 1):
        print(arr[i + 1])
        if True:
            size = i + 1
            while size != 0:
                if arr[size - 1] > arr[size]:
                    arr[size - 1], arr[size] = arr[size], arr[size - 1]
                size -= 1


insertion_sort(l)
