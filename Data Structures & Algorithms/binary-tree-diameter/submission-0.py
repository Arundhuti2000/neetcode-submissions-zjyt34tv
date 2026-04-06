# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter=0
        def length(root):
            if not root:
                return 0
            left= length(root.left)
            right=length(root.right)
            nonlocal diameter
            diameter=max(diameter, left+right)
            return 1+max(left,right)
        length(root)
        return diameter