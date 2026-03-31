class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        if self.is_same_tree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def is_same_tree(self, s: TreeNode, t: TreeNode):
        if not s and not t:
            return True
        if s and t:
            if s.val != t.val:
                return False
            return self.is_same_tree(s.left, t.left) and self.is_same_tree(s.right, t.right)
        return False
    