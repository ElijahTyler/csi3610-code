'''
recall:
A - ixj matrix
B - jxk matrix
# of multiplications = i*j*k
each of i rows in A, each of k columns in B
(i*k) -> # of pairs
(j) -> mult.s per pair

problem:
given a list of compatible matrices
A1, A2, ... , An
we want to find the product
A1A2...An
using the least number of multiplications
* matrix multiplication is associative, i.e. A1A2A3 = (A1A2)A3 = A1(A2A3)
what's the min # of multiplications required?
'''

def min_matrix_mult(p): # p = [p0, p1, ... , pn] <- sizes of matrices
    n = len(p)
    m = []
    for i in range(n+1):
        paul = []
        for j in range(n+1):
            paul.append(0)
        m.append(paul)
    print(m)
    
    for s in range(n): # gap between i and j
        for i in range(1, n-s+1): # starting matrix we're multiplying
            j = i+s
            best = float('inf')
            for k in range(i, j):
                formula = m[i][k] + m[k+1][j] + (p[i-1]*p[k]*p[j]) # table up to this point must be fully known by the time this calculation is done
                best = min(best, formula)
                m[i][j] = best
    
    return m[1][n]

min_matrix_mult([1,2,3,4,5])

# this does not work lmao
# try with memo later