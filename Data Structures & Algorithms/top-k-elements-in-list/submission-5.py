class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        values_to_num = [[] for i in range(n+1)]
        counter = Counter(nums)
        for key, value in counter.items():
            values_to_num[value].append(key)
        ans = []
        for i in range(len(values_to_num)-1, -1, -1):
            num_of_elem = len(values_to_num[i])
            for j in range(num_of_elem):
                ans.append(values_to_num[i][j])
                if len(ans)==k:
                    return ans
        return ans