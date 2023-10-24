def dfs(graph, start): # total runtime is O(|V| + |E|)
    visited = set()
    start_time = {}
    end_time = {}

    def dfs_inner(current, time): # called once for every vertex
        print(current)
        visited.add(current)
        start_time[current] = time
        time += 1
        for neighbor in graph[current]: # called twice for every edge
            if neighbor not in visited:
                dfs_inner(neighbor, time)
        end_time[current] = time
        time += 1
    
    dfs_inner(start, 0)

graph = {
    1: [2,3,4],
    2: [1,4],
    3: [1,6],
    4: [1,2,6],
    5: [7],
    6: [3,4,7],
    7: [5,6],
}

dfs(graph, 1)