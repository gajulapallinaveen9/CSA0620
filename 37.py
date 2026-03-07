# K Closest Points to Origin using sorting

def kClosest(points, k):
    # Sort points by distance from origin (x^2 + y^2)
    points.sort(key=lambda p: p[0]**2 + p[1]**2)
    return points[:k]


# Test Case 1
points1 = [[1,3],[-2,2],[5,8],[0,1]]
k1 = 2
print("Input:", points1, "k =", k1)
print("Output:", kClosest(points1, k1))

# Test Case 2
points2 = [[1,3],[-2,2]]
k2 = 1
print("\nInput:", points2, "k =", k2)
print("Output:", kClosest(points2, k2))

# Test Case 3
points3 = [[3,3],[5,-1],[-2,4]]
k3 = 2
print("\nInput:", points3, "k =", k3)
print("Output:", kClosest(points3, k3))
