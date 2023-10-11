def insertion_sort(A):
    for i in range(len(A)):
        j = i
        while j > 0 and A[j-1] > A[j]:
            A[j-1], A[j] = A[j], A[j-1]
            j -= 1

A = [3,2,5,4,6,1]
insertion_sort(A)
print(A)