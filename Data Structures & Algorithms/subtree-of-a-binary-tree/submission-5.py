# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   

    def isSameTree(self, p, q) -> bool:
        if not (p or q):
            return True
        if (not p and q) or (p and not q): return False
        return ((p.val == q.val) and 
        self.isSameTree(p.left, q.left) and 
        self.isSameTree(p.right, q.right))

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
            
        return (self.isSameTree(root, subRoot) or 
        self.isSubtree(root.left, subRoot) or
        self.isSubtree(root.right, subRoot)
        )