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
                return float('-inf')
            left_max = dfs(node.left)
            right_max = dfs(node.right)
            max_innode = max(node.val, node.val + left_max, 
            node.val + right_max)

            ans = max(ans, max_innode, node.val + left_max + right_max)
            return max_innode
        dfs(root)
        return ans

            