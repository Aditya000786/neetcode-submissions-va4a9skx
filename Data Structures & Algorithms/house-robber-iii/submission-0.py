# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from functools import lru_cache

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @lru_cache(None)
        def dfs(node):
            if not node: return 0
            curr = node.val
            if node.left:
                curr+=dfs(node.left.left)
                curr+=dfs(node.left.right)
            if node.right:
                curr+=dfs(node.right.left)
                curr+=dfs(node.right.right)
            left = dfs(node.left)
            right = dfs(node.right)
            return max(curr, left + right)
        return dfs(root)