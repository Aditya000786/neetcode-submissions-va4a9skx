# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        ans = []
        def dfs(node):
            nonlocal ans
            if not node:
                ans.append("N")
                return
            ans.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            return ans
        dfs(root)
        # print("ans", ",".join(ans))
        return ",".join(ans)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = data.split(",")
        self.i=0
        def dfs():
            if self.i>=len(nodes):
                return 
            val = nodes[self.i]
            print(self.i, val)
            if val == "N":
                self.i+=1
                return None
            node = TreeNode(int(val))
            self.i+=1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
