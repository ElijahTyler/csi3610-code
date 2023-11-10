def floyd_warshall(graph): # graph: adjacency matrix, modify in-place
    m = len(graph) # number of vertices
    dist = graph

    prev = [] # mxm matrix such that entry (i,j) contains the penultimate vertex on the minimal path from i to j
    for i in range(m):
        dave = []
        for _ in range(m):
            dave.append(i)
        prev.append(dave)

    for i in range(m): # i is the added intermediate vertex
        for u in range(m): # source vertex
            for v in range(m): # destination vertex
                if dist[u][i] + dist[i][v] < dist[u][v]:
                    dist[u][v] = dist[u][i] + dist[i][v]
                    prev[u][v] = prev[i][v]
    
    return prev
    # runtime is O(|V|^3)
    # memory complexity is O(|V|^2) with prev, O(1) without

graph = [
    [0,3,8,float('inf'),-4],
    [float('inf'),0,float('inf'),1,7],
    [float('inf'),4,0,float('inf'),float('inf')],
    [float('inf'),float('inf'),-5,0,float('inf')],
    [float('inf'),float('inf'),float('inf'),6,0]
]

prev = floyd_warshall(graph)
print(graph)
for i in range(len(prev)):
    for j in range(len(prev)):
        prev[i][j] += 1
print(prev)