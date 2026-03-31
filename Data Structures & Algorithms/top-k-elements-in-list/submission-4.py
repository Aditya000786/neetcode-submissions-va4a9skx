import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        heap = []
        for key, value in c.items():
            if len(heap)>=k:
                if heap[0][0]<value:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (value, key))
            else:
                heapq.heappush(heap, (value, key))
        return [i[1] for i in heap]