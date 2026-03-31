import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)
        counts = [-i for i in c.values()]
        heapq.heapify(counts)
        cycle = 0
        queue = deque([])
        while counts or queue:
            print("before", cycle, counts, queue)
            cycle += 1
            if counts:
                cou = -1*heapq.heappop(counts)
                cou-=1
                
                if cou>0:
                    queue.append((cycle+n, cou))
                # print("cou", cou, queue)

            
            while queue and queue[0][0]<=cycle:
                heapq.heappush(counts, -queue.popleft()[1])
            print("after", cycle, counts, queue)
        return cycle