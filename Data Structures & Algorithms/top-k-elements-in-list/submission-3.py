import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lis = [[] for i in range(len(nums) + 1)]
        cou = Counter(nums)
        for key, value in cou.items():
            lis[value].append(key)
        ans = []
        for temp in lis[::-1]:
            if k>0:
                ans+=temp
                k-=len(temp)
        return ans