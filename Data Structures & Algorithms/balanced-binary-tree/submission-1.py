# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def checkHeight(self,node):
        if not node:
            return 0
        leftHeight=self.checkHeight(node.left)
        if leftHeight == -1:
            return -1
        rightHeight=self.checkHeight(node.right)
        if rightHeight == -1:
            return -1
        if abs(leftHeight - rightHeight) > 1:
            return -1
        return 1+ max (leftHeight, rightHeight)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.checkHeight(root) != -1