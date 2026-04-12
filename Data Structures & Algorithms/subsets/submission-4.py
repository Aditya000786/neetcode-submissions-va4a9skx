class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(ind, arr):
            if ind==len(nums):
                ans.append(arr.copy())
                return ans
            arr.append(nums[ind])
            backtrack(ind+1, arr)
            arr.pop()
            backtrack(ind+1, arr)
        backtrack(0, [])
        return ans
        # res = [[]]
        # for num in nums:
        #     res += [subset + [num] for subset in res]
        # return res
        