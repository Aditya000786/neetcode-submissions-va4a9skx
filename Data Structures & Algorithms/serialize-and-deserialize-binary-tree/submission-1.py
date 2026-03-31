# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    def serialize(self, root):
        queue = deque([root])
        nodes = []
        while queue:
            curnode = queue.popleft()
            if curnode is None:
                nodes.append("N")
            else:
                nodes.append(str(curnode.val))
                queue.append(curnode.left)
                queue.append(curnode.right)
        return ",".join(nodes)

    def deserialize(self, data):
        val = data.split(",")
        if val[0] == "N":
            return None
        root = TreeNode(int(val[0]))
        queue = deque([root])
        index = 1
        while queue:
            node = queue.popleft()
            if val[index] != 'N':
                node.left = TreeNode(int(val[index]))
                queue.append(node.left)
            index+=1
            if val[index] != 'N':
                node.right = TreeNode(int(val[index]))
                queue.append(node.right)
            index+=1
        return root