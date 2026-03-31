import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        new_points = []
        for point in points:
            dist = math.sqrt(point[0]**2 + point[1]**2)
            new_points.append((-dist, point))
        heapq.heapify(new_points)
        while len(new_points)>k:
            heapq.heappop(new_points)
        return [point for dis, point in new_points]