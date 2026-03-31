class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l,r = 0,0
        heap = []
        res = []
        heapq.heapify(heap)
        while r<len(nums):
            heapq.heappush(heap, (-nums[r], r))
            r+=1
            if r-l<k:
                continue
            while heap:
                v, i = heapq.heappop(heap)
                v = -v
                if i>=l and i<=r:
                    res.append(v)
                    heapq.heappush(heap, (-v, i))
                    break
            if r-l>=k:
                l+=1
        return res