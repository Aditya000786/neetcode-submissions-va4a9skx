class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        start_num = []
        for num in nums:
            if num-1 in nums_set:
                continue
            start_num.append(num)
        max_len = 0
        ans = 0
        for num in start_num:
            temp, curr = 1, num
            while curr+1 in nums_set:
                curr += 1
                temp += 1
            ans = max(ans, temp)
        return ans