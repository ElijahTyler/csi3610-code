# heap functions

parent = lambda i: (i-1) // 2
left = lambda i: 2*i + 1
right = lambda i: 2*i + 2

def heapify_down(A, size, i):
    l = left(i)
    r = right(i)
    best = i
    while l < size:
        best = i
        if A[best] < A[l]:
            best = l
        if r < size and A[best] < A[r]:
            best = r
        if best == i:
            break
        else:
            A[best], A[i] = A[i], A[best]
            i = best
            l = left(i)
            r = right(i)

def make_heap(A, size):
    for i in range(size - 1, -1, -1):
        heapify_down(A, len(A), i)

def heapsort(A):
    make_heap(A, len(A))
    for size in range(len(A), 0, -1):
        A[size-1], A[0] = A[0], A[size-1]
        heapify_down(A, size-1, 0)



A = [4, 64, 22, 11, 19, 2, 3, 30]
heapsort(A)
print(A)