class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_nums = set(nums)
        ans = 0
        for num in nums:
            prev = num-1
            if prev in unique_nums: continue
            curr = num
            temp = 0
            while curr in unique_nums:
                temp+=1
                curr+=1
            ans = max(ans, temp)
        return ans