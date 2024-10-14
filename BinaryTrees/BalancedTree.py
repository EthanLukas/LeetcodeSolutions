# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if root is None:
            return True

        def getHeight(self, r):

            if r is None:
                return 0
            
            return 1 + max(getHeight(self, r.left), getHeight(self, r.right))
    
        return (abs(getHeight(self, root.left) - getHeight(self, root.right))<=1) and self.isBalanced(root.left) and self.isBalanced(root.right)
        

        # return isBalanced(self, root.left) and isBalanced(root.right)

        #     abs(getHeight(self, root.left) - getHeight(self, root.right) <=1)
