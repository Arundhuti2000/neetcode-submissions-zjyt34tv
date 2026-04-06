# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        result=[]
        def encode(root):
            if root is None:
                result.append("#")
                return 
            result.append(str(root.val))
            left = encode(root.left)
            right=encode(root.right)
        encode(root)
        return ",".join(result)
     

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        result=[]
        nodes_iter = iter(data.split(","))
        def buildTree():
            val= next(nodes_iter)
            if val =="#":
                return None
            node = TreeNode(int(val))
            node.left = buildTree()
            node.right = buildTree()
            return node
        return buildTree()
