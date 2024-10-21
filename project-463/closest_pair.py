import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def closest_pair(points):
    # Base case
    # if fewer than 2 points, no valid closest pair exists
    if len(points) < 2:
        return None

    if len(points) == 2:
        return points[0], points[1]

    # Split the points into two halves
    mid = len(points) // 2

    left_half = points[:mid]
    right_half = points[mid:]

    # find closest pairs on both halves
    left_closest = closest_pair(left_half)
    right_closest = closest_pair(right_half)

    # initialize min_distance and check if valid pairs were found in left or right halves

    d_min = float('inf')  # initialize to infinity

    if left_closest:
        d_min = distance(left_closest[0], left_closest[1])

    if right_closest:
        d_min = min(d_min, distance(right_closest[0], right_closest[1]))

    # find the closest pair in the strip
    mid_x = points[mid][0]  # x-coordinate of the midpoint

    strip_closest = find_strip_closest(points, mid_x, d_min)
    candidates = [pair for pair in [left_closest, right_closest, strip_closest] if pair is not None]

    # If no valid closest pairs are found, return None
    if not candidates:
        return None

    # Return the closest valid pair found
    return min(candidates, key=lambda pair: distance(pair[0], pair[1]))


def find_strip_closest(points, mid_x, d_min):
    strip = [point for point in points if abs(point[0] - mid_x) < d_min]
    strip.sort(key=lambda point: point[1])

    # Now find the closest points in the strip
    min_distance = d_min
    closest_pair = None

    # compare each point to the next 7 points
    for i in range(len(strip)):
        for j in range(i + 1, min(i + 7, len(strip))):
            d = distance(strip[i], strip[j])

            if d < min_distance:
                min_distance = d
                closest_pair = (strip[i], strip[j])

    return closest_pair