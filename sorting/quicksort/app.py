def quick_sort(sequence: list) -> list:
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    right_array, left_array = [], []

    for item in sequence:
        right_array.append(item) if item > pivot else left_array.append(item)
    return quick_sort(left_array) + [pivot] + quick_sort(right_array)


array = [10, 7, 8, 9, 1, 5]

print(quick_sort(array))
