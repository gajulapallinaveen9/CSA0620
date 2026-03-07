import itertools

cities = ["A","B","C","D","E"]

dist = [
[0,10,15,20,25],
[10,0,35,25,30],
[15,35,0,30,20],
[20,25,30,0,15],
[25,30,20,15,0]
]

start = 0
min_distance = float('inf')
best_route = None

# generate all permutations except start city
for perm in itertools.permutations(range(1,5)):
    
    current_distance = 0
    k = start
    
    for j in perm:
        current_distance += dist[k][j]
        k = j
        
    current_distance += dist[k][start]
    
    if current_distance < min_distance:
        min_distance = current_distance
        best_route = (start,) + perm + (start,)

# convert indices to city names
route = [cities[i] for i in best_route]

print("Shortest Route:", " -> ".join(route))
print("Minimum Distance:", min_distance)
