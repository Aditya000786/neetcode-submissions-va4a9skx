class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        # mem = {}
        def dfs(elem, total):
            if total>target:
                return -1

            # if total in mem:
            #     if mem[total] == -1:
            #         return -1
            #     res.add(mem[total])

            if total == target:
                s = tuple(sorted(elem))
                res.add(s)
                # mem[total] = s
            else:
                for num in nums:
                    dfs(elem+[num], total+num)
        for num in nums:
            dfs([num], num)
        return [list(r) for r in res]