# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = 0
        def dfs(node, prev_max):
            nonlocal good_nodes
            if not node:
                return
            if node.val>=prev_max:
                good_nodes+=1
            dfs(node.left, max(node.val, prev_max))
            dfs(node.right, max(node.val, prev_max))
        dfs(root, float('-inf'))
        return good_nodes
