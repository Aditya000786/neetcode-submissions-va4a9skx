import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-st for st in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            print(stones)
            st1 = heapq.heappop(stones)
            st2 = heapq.heappop(stones)
            if not st1 == st2:
                heapq.heappush(stones, abs(st1-st2)*-1)
        return 0 if len(stones)==0 else stones[0]*-1