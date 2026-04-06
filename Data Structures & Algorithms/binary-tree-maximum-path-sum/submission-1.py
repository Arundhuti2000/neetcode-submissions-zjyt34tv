# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_overall_sum = float('-inf')
    def hasMaxPathSum(self, root: Optional[TreeNode])-> int:
        if root is None:
            return 0
        
        left = self.hasMaxPathSum(root.left) 
        right = self.hasMaxPathSum(root.right)
        maxSide=max(root.val, root.val+max(left,right))
        maxCurrent= max(maxSide, root.val+left+right)
        self.max_overall_sum = max(self.max_overall_sum,maxCurrent)
        return maxSide

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.hasMaxPathSum(root)
        return self.max_overall_sum