# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        def get_height(node):
            if not node: return 0
            return 1+ max(get_height(node.left), get_height(node.right))

        is_left_balanced = self.isBalanced(root.left)
        is_right_balanced = self.isBalanced(root.right)
        if not (is_left_balanced and is_right_balanced): return False
        left_height = get_height(root.left)
        right_height = get_height(root.right)
        return True if abs(left_height-right_height)<=1 else False