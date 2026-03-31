# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        def dfs(node):
            if not node:
                return None
            node.left, node.right = dfs(node.right), dfs(node.left)
            return node
        # return dfs(root)

        def bfs(root):
            queue = deque([root])
            while queue:
                child = len(queue)
                for i in range(child):
                    node = queue.popleft()
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                    node.left, node.right = node.right, node.left
                    
        # bfs(root)

        def iterative_dfs(root):
            stack = [root]
            while stack:
                node = stack.pop()
                node.left, node.right = node.right, node.left
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        iterative_dfs(root)
        return root


