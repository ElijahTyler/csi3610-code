def selection_sort(a):
    for i in range(len(a)):
        min_index = len(a)-1
        for j in range(i, len(a)):
            if a[j] < a[min_index]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]
    return a

assert selection_sort([63, 28, 98, 84, 89, 41, 99, 2, 20, 47]) == [2, 20, 28, 41, 47, 63, 84, 89, 98, 99]
assert selection_sort([1,7,2,9,8,0,4,3,6,5]) == [0,1,2,3,4,5,6,7,8,9]