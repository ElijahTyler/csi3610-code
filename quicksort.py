def partition(A, low, high):
    pivot = A[high-1]
    i = low
    for j in range(i, high-1):
        if A[j] <= pivot:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[high-1] = A[high-1], A[i]
    return i

def quicksort(A, low, high):
    if low+1 <= high:
        mid = partition(A, low, high)
        quicksort(A, low, mid)
        quicksort(A, mid+1, high)

def quickselect(A, k):
    low, high = 0, len(A)
    mid = partition(A, low, high)
    while mid != k:
        if k < mid:
            high = mid
        if k > mid:
            low = mid+1
        mid = partition(A, low, high)
    return A[mid]



import math

A = [4, 64, 22, 11, 19, math.e, math.pi, 30]
quicksort(A, 0, len(A))
print(A)

B = [4, 64, 22, 11, 19, math.e, math.pi, 30]
print(quickselect(A, 0))