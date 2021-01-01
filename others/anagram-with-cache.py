from collections import Counter, defaultdict


def is_anagram(a, b):
    a = Counter(a)
    b = Counter(b)
    return a.items() == b.items()


def cache(arr):
    # store all anagrams together to avoid looping thro all the dictionaries
    # with the first anagram as the key of others
    # e.g if arr=['heater', 'cold', 'clod', 'cold', 'reheat', 'docl']
    # anagrams = {'heater': ['reheat'], 'cold': ['clod', 'cold', 'docl']}
    #
    anagrams = {}
    visited = []
    for i in range(len(arr)):
        if arr[i] in visited:
            continue
        visited.append(arr[i])
        anagrams[arr[i]] = []

        for j in range(1, len(arr)):
            if i == j:  # don't compare self
                continue
            if is_anagram(arr[i], arr[j]):
                visited.append(arr[j])
                anagrams[arr[i]].append(arr[j])
    return anagrams


# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY dictionary
#  2. STRING_ARRAY query
#
def string_anagram(search_list, query):
    search_anagrams = cache(search_list)

    checked = {}
    res = []

    for i in range(len(query)):
        total = 0
        # ensure that you don't calculate total anagrams
        if query[i] in checked.keys():
            res.append(checked[query[i]])
            continue
        for j in search_anagrams.keys():
            if is_anagram(query[i], j):
                total = total + len(search_anagrams[j]) + 1
        res.append(total)
        checked[query[i]] = total
    return res


if __name__ == '__main__':
    search = ['heater', 'cold', 'clod', 'cold', 'reheat', 'docl']
    q_list = ['codl', 'cold', 'heater', 'abcd', 'docl']

    print(string_anagram(search, q_list))  # [4, 4, 2, 0, 4]
