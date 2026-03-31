import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)
        i=0
        ans = None
        while i<k:
            i+=1
            ans = heapq.heappop(nums)
        return ans*-1