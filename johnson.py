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

def dijkstra(graph, source): # assume edge weight >= 0
    def min_unvisited(): # O(|V|)
        best_dist = float('inf')
        best_v = None
        for i in range(len(dist)):
            if dist[i] < best_dist:
                best_dist = dist[i]
                best_v = i
        return best_v
    
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
        
        unvisited.remove(next)
    
    return dist, prev



def johnson(graph): #graph is an adjacency list
    m = len(graph)
    new_graph = graph.copy()
    new_graph.append( [(i,0) for i in range(m)] )
    dist = bellman_ford(new_graph, m)
    mod_graph = graph.copy()

    for u in range(m): # bad code
        for idx in range(len(graph[u])):
            v, weight = graph[u][idx]
            mod_graph[u][idx] = (v, weight + dist[u]-dist[v])
    
    all_dist = []
    all_prev = []
    for s in range(m):
        s_dist, s_prev = dijkstra(mod_graph, s)
        for v in range(m):
            s_dist[v] += dist[v] - dist[s]
        all_dist.append(s_dist)
        all_prev.append(s_prev)
    
    return all_dist, all_prev