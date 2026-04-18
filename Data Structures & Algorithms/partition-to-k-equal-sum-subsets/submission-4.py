class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        ans = []
        used = set()
        target = sum(nums) // k
        if sum(nums) % k != 0:
            return False

        def dfs(ind, sub_sum, k, curr):
            if k == 0:
                return True

            if sub_sum == target:
                ans.append(curr.copy())
                if dfs(0, 0, k-1, []):
                    return True
                ans.pop()
                return False

            for i in range(ind, len(nums)):
                if i in used:
                    continue
                temp = sub_sum + nums[i]
                if temp <= target:
                    used.add(i)
                    curr.append(nums[i])
                    if dfs(i+1, temp, k, curr):
                        return True
                    curr.pop()
                    used.remove(i)
                
                if sub_sum == 0:
                    break
            return False

        res = dfs(0, 0, k, [])
        print("ans", ans)
        return res