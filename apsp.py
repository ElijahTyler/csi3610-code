def matrix_multiply(A, B, add, mult):
    # A = (p x q)
    # B = (q x r)
    # C = AB = (p x r)    
    p = len(A)
    q = len(B)
    r = len(B[0])
    
    C = [[]]

    for i in range(p):
        for j in range(r):
            C[i][j] = mult(A[i][0], B[0][j])
            for k in range(1, q):
                C[i][j] = add(C[i][j], mult(A[i][k], B[k][j]))
    
    return C

def extend_edge(A, B):
    add = lambda x,y: min(x,y)
    mult = lambda x,y: x+y
    return matrix_multiply(A, B, add, mult)

# graph === adjacency matrix
def shortest_paths_cringe(graph):
    n = len(graph)
    # L = nxn matrix with 0s on the diagonal, and infinity elsewhere

    for i in range(n-1): # enter |V|-1 times
        L = extend_edge(graph, L) # O(|V|^3)
    
    return L
    # runtime is O(|V|^4)

def shortest_paths_slightly_less_cringe(graph):
    n = len(graph)
    L = graph[:]
    i = 1

    while i < n-1: # O(ceil(lg|V|))
        L = extend_edge(L, L) # O(|V|^3)
        i *= 2
    
    return L
    # runtime is O(|V|^3 lg|V|)