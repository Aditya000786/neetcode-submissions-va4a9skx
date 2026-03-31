# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans = 0
        def bfs():
            queue = deque([root])
            while queue:
                tot = len(queue)
                for i in range(tot):
                    node = queue.popleft()

                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                ans+=1
            return ans
        
        def dfs(node):
            if not node: return 0 
            return 1 + max(dfs(node.left), dfs(node.right))
        return dfs(root)
