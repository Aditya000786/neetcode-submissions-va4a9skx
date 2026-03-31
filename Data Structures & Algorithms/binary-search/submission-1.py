class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bs(l, r):
            if l>r:
                return -1
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            if nums[mid]<target:
                return bs(mid+1, r)
            if nums[mid]>target:
                return bs(l, mid-1)
        return bs(0, len(nums)-1)