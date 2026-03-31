# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root
        ans = curr
        while curr:
            if p.val == curr.val or q.val == curr.val:
                ans = curr
                break
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
                ans = curr
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
                ans = curr
            else:
                break
        return ans            