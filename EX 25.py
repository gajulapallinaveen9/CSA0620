import math

def closest_pair(points):
    min_dist = float('inf')
    pair = (None, None)
    
    # Compare every pair of points
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            # Calculate Euclidean distance
            dist = math.sqrt((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2)
            
            # Update minimum distance and pair if needed
            if dist < min_dist:
                min_dist = dist
                pair = (points[i], points[j])
    
    return pair, min_dist


# Example usage:
points = [(1, 2), (4, 5), (7, 8), (3, 1)]
pair, min_dist = closest_pair(points)
print(f"Closest pair: {pair[0]} - {pair[1]} Minimum distance: {min_dist}")
