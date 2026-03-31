from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums: List[int]):
            if len(nums) == 0:
                return [[]]
            temp = backtrack(nums[1:])
            ans = []
            for t in temp:
                for i in range(len(t)+1):
                    copy = t.copy()
                    copy.insert(i, nums[0])
                    ans.append(copy)
                    # ans.append(t[0:i] + [nums[0]] + t[i:])
            return ans
        return backtrack(nums)