class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        queue = deque([root])
        child = 1
        while queue:
            res = []
            next_child = 0
            for i in range(child):
                node = queue.popleft()
                if node:
                    res.append(node.val)
                    if node.left:
                        next_child+=1
                        queue.append(node.left)
                    if node.right:
                        next_child+=1
                        queue.append(node.right)
            child =  next_child
            ans.append(res)
        return ans