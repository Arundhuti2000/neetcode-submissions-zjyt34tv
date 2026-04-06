# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidTree(self, node, min_bound, max_bound):
        if not node: 
            return True
        if not (min_bound<node.val<max_bound):
            return False
        isLeftValid=self.isValidTree(node.left, min_bound,node.val)
        isRightValid=self.isValidTree(node.right, node.val,max_bound)
        return isLeftValid and isRightValid

    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        return self.isValidTree(root, -float('inf'),float('inf'))