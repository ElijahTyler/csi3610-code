def binary_search_iterative(A, x):
    low = 0
    high = len(A)
    mid = high // 2
    



def binary_search_recursive(A, low, high, x):
    if low >= high: return -1 # x not in A
    mid = (low+high) // 2
    if A[mid] == x:
        return mid
    if x > A[mid]:
        return binary_search_recursive(A, mid+1, high, x)
    else:
        return binary_search_recursive(A, low, mid, x)
    
A = [1, 2, 3, 4, 5, 6, 7, 8]
res = binary_search_recursive(A, 0, len(A), 3)
print(res)