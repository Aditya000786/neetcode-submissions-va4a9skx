class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        is_balanced = True

        def dfs(node):
            nonlocal is_balanced
            if not node: return 0
            l = dfs(node.left)
            r = dfs(node.right)
            d = abs(l-r)
            if d>1:
                is_balanced = False
            return 1+ max(l, r)
        dfs(root)
        return is_balanced