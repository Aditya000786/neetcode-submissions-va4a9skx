class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        coun = Counter(nums)
        heap = []
        ans = []
        for key, val in coun.items():
            heapq.heappush(heap, (-val, key))
        while k>0 and heap:
            val, key = heapq.heappop(heap)
            ans.append(key)
            k-=1
        return ans