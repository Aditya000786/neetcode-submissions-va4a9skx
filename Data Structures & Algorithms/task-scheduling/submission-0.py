from collections import Counter, deque
from typing import List
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        c:Counter = Counter(tasks)
        heap = [-value for value in c.values()]
        heapq.heapify(heap)
        queue = deque()
        while heap or queue:
            time+=1
            if heap:
                coun = 1+heapq.heappop(heap)
                if coun:
                    queue.append((coun, time+n))
            
            if queue and queue[0][1]==time:
                heapq.heappush(heap, queue.popleft()[0])
        return time  