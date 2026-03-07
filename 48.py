import sys

N = 4

def tsp(graph, visited, pos, count, cost):

    if count == N:
        return cost + graph[pos][0]

    ans = sys.maxsize

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            new_cost = tsp(graph, visited, i, count+1, cost + graph[pos][i])
            ans = min(ans, new_cost)
            visited[i] = False

    return ans


def find_min_path(graph):
    visited = [False]*N
    visited[0] = True
    return tsp(graph, visited, 0, 1, 0)


# Test Case 1
graph1 = [
[0,10,15,20],
[10,0,35,25],
[15,35,0,30],
[20,25,30,0]
]

print("Test Case 1 Output:", find_min_path(graph1))


# Test Case 2
graph2 = [
[0,10,10,10],
[10,0,10,10],
[10,10,0,10],
[10,10,10,0]
]

print("Test Case 2 Output:", find_min_path(graph2))


# Test Case 3
graph3 = [
[0,1,2,3],
[1,0,4,5],
[2,4,0,6],
[3,5,6,0]
]

print("Test Case 3 Output:", find_min_path(graph3))
