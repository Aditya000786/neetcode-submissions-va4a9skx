class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, min_val, max_val):
            if not node: return True
            if node.val>=max_val or node.val<=min_val: return False
            return (
                dfs(node.left, min_val, min(max_val, node.val))
                and 
                dfs(node.right, max(min_val, node.val), max_val))
        return dfs(root, float('-inf'), float('inf'))