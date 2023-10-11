def example_function(A):
    total = 0
    for i in range(len(A)):
        for j in range(i, len(A)):
            total += A[j]
    return total