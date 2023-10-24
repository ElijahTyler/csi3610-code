from collections import deque

def bfs(graph, start): # total runtime is O(|V| + |E|)
    discovered = set()
    queue = deque()
    queue.append(start)
    discovered.add(start)

    while len(queue) > 0: # enter loop for every reachable vertex from start -> O(|V|)
        current = queue.popleft() # O(1)
        print(current)
        
        for next in graph[current]: # enter loop for every edge of every reachable vertex -> O(|E|)
            if next not in discovered: # O(1)
                discovered.add(next)
                queue.append(next)

graph = {
    1: [2,3,4],
    2: [1,4],
    3: [1,6],
    4: [1,2,6],
    5: [7],
    6: [3,4,7],
    7: [5,6],
}

paul = bfs(graph, 1)