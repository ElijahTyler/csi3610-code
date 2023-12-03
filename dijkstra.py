def dijkstra(graph, source): # assume edge weight >= 0
    def min_unvisited(): # O(|V|)
        best_dist = float('inf')
        best_v = None
        for i in range(len(dist)):
            if dist[i] < best_dist:
                best_dist = dist[i]
                best_v = i
        return best_v
    
    def min_unvisited_heap():
        # to implement with heap, we need a decrease_key() function that reduces a value in a heap
        # to decrease a node in a heap, replace its value and heapify_up -> O(lg n)
        # AND we need to maintain a lookup table for where each vertex is on the heap
        return 'eli'
    
    def relax(v1, v2, weight): # O(1)
        if dist[v1]+weight < dist[v2]:
            dist[v2] = dist[v1]+weight
            prev[v2] = v1
    
    dist = []
    prev = []
    for _ in range(len(graph)): # O(|V|)
        dist.append(float('inf'))
        prev.append(None)

    dist[source] = 0
    unvisited = set(range(len(graph)))
    while len(unvisited): # O(|V|)
        next = min_unvisited() # O(|V|)

        if dist[next] == float('inf'): # disconnected graph
            break
        
        for weight, target in graph[next]:
            relax(next, target, weight) # called once per every edge, O(|E|)
        
        try:
            unvisited.remove(next)
        except:
            pass
    
    return dist, prev
    # runtime w/ linear search
    # = (# of searches)(time per search)+(every edge relaxed once)
    # = |V||V|+|E|
    # but |E| <= |V|^2 for any graph
    # runtime = O(|V|^2)

    # |E| <= |V|^2 for any graph
    # lg |E| <= lg |V|^2
    #        = 2 lg |V|
    # lg |E| = O(lg |V|)

    # runtime w/ heap
    # = (# of searches)(removing min element from heap)+(each edge considered)(time to decrease heap key)
    # = |V| lg |V| + |E| lg |V|
    # = O( (|V| + |E|) lg |V| )



graph = { # source: [(weight, target), ...]
    0: [(2, 3), (7, 4), (6, 5)],
    1: [(4, 2), (8, 3)],
    2: [(4, 1), (11, 3), (8, 4)],
    3: [(8, 1), (11, 2), (2, 0), (1, 5)],
    4: [(8, 2), (7, 0), (7, 5)],
    5: [(1, 3), (6, 0), (4, 6), (2, 7)],
    6: [(7, 4), (4, 5), (14, 7), (9, 8)],
    7: [(2, 5), (14, 6), (10, 8)],
    8: [(9, 6), (10, 7)],
}

paul = dijkstra(graph, 0)
print(paul)