import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for index, (x,y) in enumerate(points):
            distances.append((math.sqrt(x**2 + y**2), index))
        heapq.heapify(distances)
        ans = []
        for i in range(k):
            ans.append(points[heapq.heappop(distances)[1]])
        return ans