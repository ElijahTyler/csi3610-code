#Edmonds-Karp Algorithm
def max_flow(capacities, source, sink):
        n = len(capacities) # C is the capacity matrix
        flows = [[0] * n for i in range(n)]
        path = bfs(capacities, flows, source, sink)
      #  print path
        while path != None:
            flow = min(capacities[u][v] - flows[u][v] for u,v in path)
            for u,v in path:
                flows[u][v] += flow
                flows[v][u] -= flow
            path = bfs(capacities, flows, source, sink)
        return sum(flows[source][i] for i in range(n))

#find path by using BFS
def bfs(capacities, flows, source, sink):
        queue = [source]
        paths = {source:[]}
        if source == sink:
            return paths[source]
        while queue: 
            u = queue.pop(0)
            for v in range(len(capacities)):
                    if(capacities[u][v]-flows[u][v]>0) and v not in paths:
                        paths[v] = paths[u]+[(u,v)]
                        print(paths)
                        if v == sink:
                            return paths[v]
                        queue.append(v)
        return None
    
C = [
    [0, 10, 0, 10, 0, 0],
    [0, 0, 4, 2, 8, 0],
    [0, 0, 0, 0, 0, 10],
    [0, 0, 0, 0, 9, 0],
    [0, 0, 6, 0, 0, 10],
    [0, 0, 0, 0, 0, 0]
]

source = 0  # A
sink = 5    # F
paul = max_flow(C, source, sink)
print("max flow:", paul)