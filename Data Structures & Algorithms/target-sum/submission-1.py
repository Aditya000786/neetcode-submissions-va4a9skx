class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = []
        def dfs(ind, dic={}) -> dict:
            if ind == -1:
                return dic
            if ind == len(nums)-1:
                temp = {}
                temp[nums[ind]]=1
                if -nums[ind] in temp:
                    temp[-nums[ind]]+=1
                else:
                    temp[-nums[ind]] = 1
                return dfs(ind-1, temp)
            else:
                temp = {}
                for num, cou in dic.items():
                    t = num + nums[ind]
                    if t in temp:
                        temp[t]+=cou
                    else:
                        temp[t] = cou
                    
                    t = num - nums[ind]
                    if t in temp:
                        temp[t]+=cou
                    else:
                        temp[t] = cou
                return dfs(ind-1, temp)
        a = dfs(len(nums)-1, {})
        if target in a:
            return a[target]
        else:
            return 0