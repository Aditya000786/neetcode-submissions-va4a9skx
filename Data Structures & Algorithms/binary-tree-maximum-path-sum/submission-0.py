class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')
        def dfs(node: Optional[TreeNode]):
            nonlocal res
            if not node:
                return float('-inf')
            else:
                left_max_sum  = dfs(node.left)
                right_max_sum = dfs(node.right)
                left_max_sum = max(left_max_sum, 0)
                right_max_sum = max(right_max_sum, 0)
                res = max(res, left_max_sum + right_max_sum + node.val)
                return node.val + max(left_max_sum, right_max_sum)
        dfs(root)
        return res
