# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self,node,depth,result):
            if not node:
                return []
            if depth == len(result):
                result.append(node.val)
            self.helper(node.right, depth+1, result)
            self.helper(node.left, depth+1, result)
            
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        self.helper(root,0,result)
        return result