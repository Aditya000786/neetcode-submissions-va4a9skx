import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_arr = []
        res = []
        l=0
        for i in range(k-1):
            heapq.heappush(max_arr, (-nums[i], i))

        for r in range(k-1, len(nums)):
            heapq.heappush(max_arr, (-nums[r], r))
            num_val, num_ind = heapq.heappop(max_arr)
            while l>num_ind:
                num_val, num_ind = heapq.heappop(max_arr)
            res.append(-num_val)
            heapq.heappush(max_arr, (num_val, num_ind))
            l+=1
        return res