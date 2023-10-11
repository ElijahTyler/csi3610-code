def cringe_max_subarray(A): # O(n^3)
    best = float('-inf')
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            if best < sum(A[i:j]):
                best = sum(A[i:j])
    return best

A = [1, 7, 3, -2, 0, 7, -5, 8, 4]
paul = cringe_max_subarray(A)
print(paul)

def cooler_max_crossing(A, low, mid, high):
    right_end = mid
    right_best = A[mid]
    right_total = A[mid]
    for i in range(mid+1, high):
        right_total += A[i]
        if right_total > right_best:
            right_best = right_total
            right_end = i
    left_start = mid - 1
    left_best = A[mid - 1]
    left_total = A[mid - 1]
    for i in range(mid-2, low-1, -1):
        left_total += A[i]
        if left_total > left_best:
            left_best = left_total
            left_start = i
    return left_start, right_end, left_best + right_best

def cooler_max_subarray(A, low, high):
    if high-low == 1:
        return low, low, A[low]
    mid = (low+high) // 2

    left_low, left_high, left_sum = cooler_max_subarray(A, low, mid)
    right_low, right_high, right_sum = cooler_max_subarray(A, mid, high)
    cross_low, cross_high, cross_sum = cooler_max_crossing(A, low, mid, high)
    
    if right_sum > cross_sum:
        if left_sum > right_sum:
            return left_low, left_high, left_sum
        return right_low, right_high, right_sum
    return cross_low, cross_high, cross_sum

A = [1, 7, 3, -2, 0, 7, -5, 8, 4]
paul = cooler_max_subarray(A, 0, len(A))
print(paul)