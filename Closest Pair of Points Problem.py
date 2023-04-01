import math
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
def brute_force(points):
    n = len(points)
    min_dist = float('inf')
    
    for i in range(n-1):
        for j in range(i+1, n):
            dist = distance(points[i], points[j])
            
            if dist < min_dist:
                min_dist = dist
    return min_dist

def closest_pair(points):
    n = len(points)
    if n <= 3:
        return brute_force(points)
    mid = n // 2
    left_points = points[:mid]
    right_points = points[mid:]
    left_min = closest_pair(left_points)
    right_min = closest_pair(right_points)
    min_dist = min(left_min, right_min)
    mid_point = (points[mid-1][0] + points[mid][0]) / 2
    strip = []
    for point in points:
        if abs(point[0] - mid_point) < min_dist:
            strip.append(point)
    strip_min = strip_distance(strip, min_dist)
    return min(min_dist, strip_min)

def strip_distance(strip, d):
    min_dist = d
    strip.sort(key=lambda point: point[1])
    n = len(strip)
    for i in range(n-1):
        for j in range(i+1, n):
            if strip[j][1] - strip[i][1] > min_dist:
                break
            dist = distance(strip[i], strip[j])
            if dist < min_dist:
                min_dist = dist
    return min_dist
