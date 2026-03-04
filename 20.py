import heapq
from collections import defaultdict

def dijkstra_edge_list(n, edges, source, target):
    graph = defaultdict(list)
    for u,v,w in edges:
        graph[u].append((v,w))

    pq = [(0, source)]
    dist = {i: float('inf') for i in range(n)}
    dist[source] = 0

    while pq:
        d,u = heapq.heappop(pq)
        if u == target:
            return d
        if d > dist[u]:
            continue
        for v,w in graph[u]:
            if dist[v] > d + w:
                dist[v] = d + w
                heapq.heappush(pq,(dist[v],v))

    return -1


# Test
edges = [(0,1,7),(0,2,9),(0,5,14),(1,2,10),(1,3,15),
         (2,3,11),(2,5,2),(3,4,6),(4,5,9)]

print(dijkstra_edge_list(6, edges, 0, 4))  # Output: 20
