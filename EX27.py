import itertools
import math

# 1. Distance function
def distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    return math.sqrt((city1[0]-city2[0])**2 + (city1[1]-city2[1])**2)

# 2. TSP function (exhaustive search)
def tsp(cities):
    n = len(cities)
    start = cities[0]  # fix the first city as starting point
    other_cities = cities[1:]
    
    min_dist = float('inf')
    best_path = None
    
    # Generate all permutations of the remaining cities
    for perm in itertools.permutations(other_cities):
        path = [start] + list(perm) + [start]  # complete cycle
        # Calculate total distance
        total_dist = sum(distance(path[i], path[i+1]) for i in range(len(path)-1))
        
        if total_dist < min_dist:
            min_dist = total_dist
            best_path = path
    
    return min_dist, best_path


# -------------------------------
# Example usage
cities = [(0,0), (1,2), (4,0), (6,3)]
min_dist, best_path = tsp(cities)

print("Shortest path:", best_path)
print("Minimum distance:", min_dist)
