def max_subarray(A):
    max_global = A[0]
    max_current = A[0]

    for i in range(1, len(A)):
        max_current = max( max_current + A[i], A[i] )
        max_global = max( max_current, max_global )
    
    return max_global

A = [4, 7, -2, 0, 3, -14, 2, 8]
paul = max_subarray(A)
print(paul)

_='''
loop invariant:
- max_global is the largest subarray sum in A[0:i]
- max_current is the largest subarray sum ending at A[i-1]
initialization:
look at the code lol
maintenance:
the best subarray ending at A[i] is either:
- A[i] itself
- a continuation of the best ending at A[i-1]
the best subarray for A[:i+1] is either the best for A[:i] or it ends at A[i]
termination:
when i=n, the max_global has the best subarray in A[0:n] = A
'''