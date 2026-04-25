class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        curr = []
        visited_ind = set()
        def dfs():
            if len(curr) == len(nums):
                ans.append(curr.copy())
                return

            for i in range(len(nums)):
                if i in visited_ind: continue
                visited_ind.add(i)
                curr.append(nums[i])
                dfs()
                visited_ind.remove(i)
                curr.pop()
            return
        dfs()
        return ans