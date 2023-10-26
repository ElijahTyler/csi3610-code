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

def heap_add(A, element):
    A.append(element)
    make_heap(A, len(A))

def remove_min(A):
    paul = A.pop(0)
    heapify_down(A, len(A), 0)
    return paul



# all graphs are adjacency lists unless otherwise noted

def prim(graph, start):
    visited = set() # alt. to "set()" class is is_visited = [False]*|V| -> O(|V|) time and memory
    mst = [] # list of edges for the minimal spanning tree
    
    # maintain a list of candidate edges to choose next
    # select the minimal weight edge from the list, then:
    # - visit that vertex, and
    # - add all of its edges to the candidate list

    edges = [] # store edges, ordered by weight in a min-heap
    visited.add(start)
    
    for (neighbor, weight) in graph[start]: # O(|E|)
        heap_add(edges, (weight, start, neighbor))# O(lg |E|)
    
    while len(edges) > 0: # enter loop |E| times
        current, prev, weight = remove_min(edges) # O(lg n)
        if current not in visited: # "pass" if statement |V|-1 times
            visited.add(current) # O(1)
            mst.append((prev, current, weight)) # O(1)
            for (new_neighbor, weight) in graph[current]: # called for every edge in G, O(|E|)
                heap_add(edges, (weight, current, new_neighbor)) # O(lg |E|)
    
    return mst
    # runtime is O(|E| lg |E|) for a connected graph
    # memory is O(|E|) for a connected graph



graph = {
    'a': [(1, 'b'),(4, 'd')],
    'b': [(1, 'a'),(2, 'c')],
    'c': [(2, 'b')],
    'd': [(4, 'a')]
}

paul = prim(graph, 'a')
print(paul)