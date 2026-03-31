class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def get_max_depth(node: Optional[TreeNode]):
            if not node:
                return 0
            left_height = get_max_depth(node.left)
            right_height = get_max_depth(node.right)
            return max(left_height, right_height)+1
        return get_max_depth(root)