class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1
        ans = float('inf')

        while low<=high:
            mid = (low + high) // 2
            if nums[0]<=nums[mid]:
                ans = min(ans, nums[0])
                low = mid+1
            if mid+1<=high and nums[mid+1]<=nums[high]:
                ans = min(ans, nums[mid+1])
                high = mid
        return ans