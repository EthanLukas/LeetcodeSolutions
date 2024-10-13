# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root is None:
            return None

        r = root
        
        temp = r.left

        r.left = r.right
        r.right = temp

        self.invertTree(r.left)
        self.invertTree(r.right)

        # while curr.left is not None and curr.right is not None:
            

        return r


        
        