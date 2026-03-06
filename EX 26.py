import math

# Closest Pair of Points (Brute Force)
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def closest_pair(points):
    min_dist = float('inf')
    pair = None
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            dist = euclidean_distance(points[i], points[j])
            if dist < min_dist:
                min_dist, pair = dist, (points[i], points[j])
    return pair, min_dist


# Convex Hull (Brute Force)
def orientation(p, q, r):
    return (q[1]-p[1])*(r[0]-q[0]) - (q[0]-p[0])*(r[1]-q[1])

def convex_hull(points):
    hull = set()
    n = len(points)
    for i in range(n):
        for j in range(i+1, n):
            left = right = False
            for k in range(n):
                if k != i and k != j:
                    val = orientation(points[i], points[j], points[k])
                    if val > 0: left = True
                    elif val < 0: right = True
            if not (left and right):  # all points on one side
                hull.add(points[i]); hull.add(points[j])
    return list(hull)


# -------------------------------
# Test Closest Pair
points1 = [(1,2),(4,5),(7,8),(3,1)]
pair, dist = closest_pair(points1)
print("Closest pair:", pair, "Distance:", dist)

# Test Convex Hull
points2 = [(10,0),(11,5),(5,3),(9,3.5),(15,3),(12.5,7),(6,6.5),(7.5,4.5)]
hull = convex_hull(points2)
print("Convex Hull:", hull)
