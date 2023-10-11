def merge(a_1, a_2):
    result = []
    i, j = 0, 0
    while i < len(a_1) and j < len(a_2):
        if a_1[i] <= a_2[j]: # "at most" makes merge_sort stable, i.e. elements with the same value never switch places
            result.append(a_1[i])
            i += 1
        else:
            result.append(a_2[j])
            j += 1
    while i < len(a_1):
        result.append(a_1[i])
        i += 1
    while j < len(a_2):
        result.append(a_2[j])
        j += 1
    return result

def merge_sort(a):
    if len(a) == 1:
        return a
    midpt = len(a) // 2
    a_1 = merge_sort(a[:midpt])
    a_2 = merge_sort(a[midpt:])
    return merge(a_1, a_2)

assert merge_sort([0, 4, 1, 5, 2, 6, 3, 7]) == [0, 1, 2, 3, 4, 5, 6, 7]
assert merge_sort([63, 28, 98, 84, 89, 41, 99, 2, 20, 47]) == [2, 20, 28, 41, 47, 63, 84, 89, 98, 99]