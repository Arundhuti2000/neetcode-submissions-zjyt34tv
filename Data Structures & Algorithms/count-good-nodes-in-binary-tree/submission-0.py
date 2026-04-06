# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def backtrack(self, curr_max, X):
        if not X:
            return 0
        count=0
        if X.val>=curr_max:
            count=1
        curr_max=max(curr_max,X.val)
        count+=self.backtrack(curr_max, X.left)
        count+=self.backtrack(curr_max, X.right)
        return count 
    def goodNodes(self, root: TreeNode) -> int:
        curr_max=root.val
        count=0
        return self.backtrack(curr_max, root)