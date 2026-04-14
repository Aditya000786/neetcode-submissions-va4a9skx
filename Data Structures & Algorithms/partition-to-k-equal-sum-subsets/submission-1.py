class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0: return False
        target = total // k
        ans = []
        used = [False] * len(nums)
        curr = []
        def backtrack(ind, k, subsetSum):
            if k == 0:
                return True
            if subsetSum == target:
                return backtrack(0, k-1, 0)
            
            for j in range(ind, len(nums)):
                if used[j] or nums[j] + subsetSum>target:
                    continue
                used[j] = True
                if backtrack(j+1, k, nums[j] + subsetSum):
                    return True
                used[j] = False
            return False
        return backtrack(0, k, 0)
        