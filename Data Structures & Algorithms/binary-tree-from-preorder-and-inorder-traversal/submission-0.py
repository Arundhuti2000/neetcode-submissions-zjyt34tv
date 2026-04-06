# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTreeHelper(self,preorder, inorder, inorderstart,inorderend):
        if inorderstart>inorderend:
            return None
        rootvalue= preorder[self.preOrderIndex]
        root = TreeNode(rootvalue)
        rootIndex= self.inOrderMap[rootvalue]
        self.preOrderIndex+=1
        root.left = self.buildTreeHelper(preorder, inorder, inorderstart, rootIndex-1)
        root.right= self.buildTreeHelper(preorder, inorder, rootIndex+1, inorderend)
        return root
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preOrderIndex = 0
        self.inOrderMap={}
        for i  in range (len(inorder)):
            self.inOrderMap[inorder[i]]=i
        return self.buildTreeHelper(preorder, inorder, 0,len(inorder)-1)