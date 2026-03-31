class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = []
        def dfs(node: Optional[TreeNode]):
            if node:
                dfs(node.left)
                res.append(node.val)
                dfs(node.right)
            else:
                return
        dfs(root)
        for i in range(1, len(res)):
            if res[i]<=res[i-1]:
                return False
        # return res
        return True