import heapq


def heap_sort(iterable):
    h = []

    for value in iterable:
        heapq.heappush(h, value)

    return [heapq.heappop(h) for i in range(len(h))]


# sort a list of array
iterable = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]

heap_sort(iterable)
iterable.sort()
