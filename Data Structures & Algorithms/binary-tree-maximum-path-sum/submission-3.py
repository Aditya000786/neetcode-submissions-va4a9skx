# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float('-inf')
        def dfs(node):
            nonlocal ans
            if not node:
                return 0
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            ans = max(ans, left_sum+right_sum+node.val, node.val, left_sum+node.val,
                    right_sum+node.val)
            return max(node.val, left_sum+node.val, right_sum+node.val)
        dfs(root)
        return ans