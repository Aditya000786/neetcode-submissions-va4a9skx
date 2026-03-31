# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.p_arr, self.q_arr = [],[]
        def inOrder(node: Optional[TreeNode], arr):
            if not node:
                arr.append(None)
                return
            arr.append(node.val)
            inOrder(node.left, arr)
            inOrder(node.right, arr)
        inOrder(p, self.p_arr)
        inOrder(q, self.q_arr)
        return self.p_arr == self.q_arr
