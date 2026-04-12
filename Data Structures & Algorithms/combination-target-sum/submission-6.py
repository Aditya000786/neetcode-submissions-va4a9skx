class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        curr = []
        def backtrack(ind, total):
            if total > target or ind==len(nums):
                return
            if total ==  target:
                ans.append(curr.copy())
                return
            curr.append(nums[ind])
            backtrack(ind, total+nums[ind])
            curr.pop()
            j =ind+1
            while j<len(nums) and nums[j] == nums[ind]:
                j+=1
            backtrack(j, total)
            return
        backtrack(0, 0)
        return ans