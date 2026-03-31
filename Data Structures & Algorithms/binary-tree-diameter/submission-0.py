# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = float('-infinity')
        def get_diam(node: Optional[TreeNode]) -> int:
            nonlocal ans
            if not node:
                return 0 
            else:
                left_diam = get_diam(node.left)
                right_diam = get_diam(node.right)
                ans = max(ans, left_diam + right_diam+1)
                print("ans", ans)
                return max(left_diam,right_diam)+1
        aa = get_diam(root)
        ans = max(ans, aa)
        return ans - 1