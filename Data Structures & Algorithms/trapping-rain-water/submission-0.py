from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left_side_prefix = [None]*len(height)
        right_side_prefix = [None]*len(height)
        max_height = float('-inf')
        for i in range(len(height)):
            left_side_prefix[i]= max(max_height, height[i])
            max_height = max(max_height, height[i])
            
        max_height = float('-inf')
        for i in range(len(height)-1, -1, -1):
            right_side_prefix[i] = max(max_height, height[i])
            max_height = max(max_height, height[i])

        ans = 0
        for i in range(len(height)):
            curr_left_side_prefix = left_side_prefix[i]
            curr_right_side_prefix = right_side_prefix[i]
            ans += min(curr_left_side_prefix, curr_right_side_prefix) - height[i]
        return ans