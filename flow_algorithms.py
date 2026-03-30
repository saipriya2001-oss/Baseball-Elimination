from collections import deque

def bfs(capacity, flow, source, sink, parent):
    """
    Breadth-First Search for Edmonds-Karp Max-Flow.
    """
    visited = set()
    queue = deque([source])
    visited.add(source)

    while queue:
        u = queue.popleft()

        for v in capacity.get(u, {}):
            if v not in visited and (capacity[u][v] - flow[u][v] > 0):
                parent[v] = u
                visited.add(v)
                queue.append(v)
                if v == sink:
                    return True
    return False

def edmonds_karp(capacity, source, sink):
    """
    Finds the maximum flow in a network using the Edmonds-Karp algorithm.
    """
    flow = {}
    for u in capacity:
        flow[u] = {}
        for v in capacity[u]:
            flow[u][v] = 0

    total_flow = 0
    parent = {}

    while bfs(capacity, flow, source, sink, parent):
        path_flow = float('inf')
        s = sink
        while s != source:
            p = parent[s]
            path_flow = min(path_flow, capacity[p][s] - flow[p][s])
            s = p

        total_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            flow[u][v] += path_flow
            
            if v not in flow:
                flow[v] = {}
            if u not in flow[v]:
                flow[v][u] = 0
                
            flow[v][u] -= path_flow
            v = u
            
    return total_flow, flow
