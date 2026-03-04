import sys

def dijkstra(graph, src):
    n = len(graph)
    dist = [sys.maxsize]*n
    visited = [False]*n
    dist[src] = 0

    for _ in range(n):
        u = min((d,i) for i,d in enumerate(dist) if not visited[i])[1]
        visited[u] = True

        for v in range(n):
            if graph[u][v] != float('inf') and not visited[v]:
                dist[v] = min(dist[v], dist[u] + graph[u][v])

    return dist


# Test
graph = [
[0,10,3,float('inf'),float('inf')],
[float('inf'),0,1,2,float('inf')],
[float('inf'),4,0,8,2],
[float('inf'),float('inf'),float('inf'),0,7],
[float('inf'),float('inf'),float('inf'),9,0]
]

print(dijkstra(graph,0))  # Output: [0,7,3,9,5]
