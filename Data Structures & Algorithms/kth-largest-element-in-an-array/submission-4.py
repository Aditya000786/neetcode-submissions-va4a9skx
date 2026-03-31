class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        def quickselect(l,r):
            p, pivot = l, nums[r]
            for i in range(l,r):
                if nums[i]<pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p+=1
            nums[r], nums[p] = nums[p], nums[r]
            if k<p: return quickselect(l, p-1)
            elif k>p: return quickselect(p+1, r)
            else: return nums[p]
        return quickselect(0, len(nums)-1)