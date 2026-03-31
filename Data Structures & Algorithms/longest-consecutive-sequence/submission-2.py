class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        di = Counter(nums)
        ans = 0
        for num in nums:
            if num-1 in di:
                continue
            else:
                temp_ans = 0
                while num in di:
                    temp_ans+=1
                    num+=1
                ans = max(ans, temp_ans)
        return ans
# Convert the whole thing into a set
# Traverse the array find the element whose previous element dosent exist
# For each of those element try to make the list as big as possible.
# Return the length of the max list that was possible.