from DisjointSet import DisjointSet

def kruskal(graph):
    sets = DisjointSet()

    for i in range(len(graph)):
        sets.make_set(i) # |V| calls to sets.make_set
    
    edges = []

    # O(|E| + |V|)
    for source in range(len(graph)):
        for weight, target in graph[source]:
            if source < target: #de-duplicating edges
                edges.append((weight, source, target))
    
    edges.sort() # O(|E| lg |E|)
    
    mst = []
    
    for weight, v1, v2 in edges: # enter |E| times
        if sets.find(v1) != sets.find(v2): # 2 calls to sets.find per loop
            mst.append((v1, v2, weight)) # both f.ns at most |V|-1 times (if graph is connected)
            sets.union(v1, v2)
    
    return mst
    # total number of DisjointSet operations is |V| + 2|E| + |V|-1 = THETA(|V|+|E|)
    # runtime of DisjointSet is O(|E|alpha(|E|))
    # alpha|E| is almost constant
    # assume |E|>|V|, i.e. graph connected
    # total: |E| lg |E| + |E|alpha(|E|) = O(|E| lg |E|)



graph = {
    'a': [(4, 'b'), (8, 'c')],
    'b': [(4, 'a'), (11, 'c'), (8, 'e')],
    'c': [(8, 'a'), (11, 'b'), (2, 'd'), (1, 'f')],
    'd': [(2, 'c'), (7, 'e'), (6, 'f')],
    'e': [(8, 'b'), (7, 'd'), (7, 'f')],
    'f': [(1, 'c'), (6, 'd'), (4, 'g'), (2, 'h')],
    'g': [(7, 'e'), (4, 'f'), (14, 'h'), (9, 'i')],
    'h': [(2, 'f'), (14, 'g'), (10, 'i')],
    'i': [(9, 'g'), (10, 'h')],
}

graph = { # source: [(weight, target), ...]
    0: [(4, 1), (8, 2)],
    1: [(4, 0), (11, 2), (8, 4)],
    2: [(8, 0), (11, 1), (2, 3), (1, 5)],
    3: [(2, 2), (7, 4), (6, 5)],
    4: [(8, 1), (7, 3), (7, 5)],
    5: [(1, 2), (6, 3), (4, 6), (2, 7)],
    6: [(7, 4), (4, 5), (14, 7), (9, 8)],
    7: [(2, 5), (14, 6), (10, 8)],
    8: [(9, 6), (10, 7)],
}

paul = kruskal(graph)
print(paul)