class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        max1, min1 = nums[0], nums[0]
        for i in range(1, len(nums)):
            t1 = max(nums[i], min1*nums[i], max1*nums[i])
            t2 = min(nums[i], min1*nums[i], max1*nums[i])
            if t1>t2:
                max1, min1 = t1, t2
            else:
                max1, min1 = t2, t1
            # print(i, max1, min1)
            ans = max(max1, ans)
        return ans