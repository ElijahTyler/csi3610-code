from queue import deque

def bfs(graph, start):
    discovered = set()
    queue = deque()
    queue.pushright(start)
    discovered.add(start)