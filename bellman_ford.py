def bellman_ford(graph, source):
    n = len(graph)    

    dist = []
    prev = []
    for _ in range(n):
        dist.append(float('inf'))
        prev.append(None)
    dist[source] = 0

    def relax(v1, v2, weight): # O(1)
        if dist[v1]+weight < dist[v2]:
            dist[v2] = dist[v1]+weight
            prev[v2] = v1

    # find all min paths w/o negative cycles
    for _ in range(n - 1): # enter |V|-1 times
        for v1 in range(n): # enter |E| times
            for (v2, weight) in graph[v1]:
                relax(v1, v2, weight)
                
                # if nothing changes in the iteration, alg. is done

    # check for negative cycles
    for v1 in range(n): # enter |E| times
        for (v2, weight) in graph[v1]:
            if dist[v1]+weight < dist[v2]:
                return False
    
    return dist, prev
    # runtime is Θ(|V||E|)