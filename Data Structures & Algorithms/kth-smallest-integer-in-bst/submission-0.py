# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values = []
        def preorder(node):
            if not node:
                return
            preorder(node.left)
            values.append(node.val)
            preorder(node.right)
        preorder(root)
        return values[k-1]