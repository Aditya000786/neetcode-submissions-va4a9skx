class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        curr = []
        def backtrack(comb):
            if len(comb)==1:
                ans.append(curr+comb)
                return
            
            for i in range(len(comb)):
                curr.append(comb[i])
                backtrack(comb[:i] + comb[i+1:])
                curr.pop()

        backtrack(nums)
        return ans