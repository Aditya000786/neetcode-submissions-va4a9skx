import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        coun = Counter(nums)
        lis = []
        for key, value in coun.items():
            lis.append((-value, key))
        heapq.heapify(lis)
        ans = []
        while k>0:
            val, key = heapq.heappop(lis)
            ans.append(key)
            k-=1
        return ans