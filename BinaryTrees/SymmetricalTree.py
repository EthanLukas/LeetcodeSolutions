# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:


        # def invertTree(self, r):

        #     if root is None:
        #         return

        #     temp = r.left
        #     r.left = r.right
        #     r.right = temp

        #     invertTree(self, r.left)
        #     invertTree(self, r.right)         

        # def checkSame(self, l, r):

        #     print(l)
        #     print(r)

        #     if l is None and r is None:
        #         return True
            
        #     elif l is None or r is None:
        #         return False

        #     elif l.val != r.val:
        #         return False

        #     elif (l.left is None and r.right is not None) or (l.left is not None and r.right is None):
        #         return False

        #     elif (l.right is None and r.left is not None) or (l.right is not None and r.left is None):
        #         return False

        #     elif l.left is None and l.right is None and r.left is None and r.right is None:
        #         return True

        #     elif l.left.val != r.right.val or l.right.val != r.left.val:
        #         return False

        #     return (checkSame(self, l.left, r.right) and checkSame(self, l.right, r.left))
        

        # # Length one
        # if root.left is None and root.right is None:
        #     return True

        # # Invert one side of the tree, then check if the same 
        # # invertTree(self, root.right)

        # # Check if both sides symmetrical
        # return checkSame(self, root.left, root.right)
        # # return True

        def checkSame(self, l, r):

            if l is None and r is None:
                return True
            
            elif l is None or r is None:
                return False

            elif l.val != r.val:
                return False

            return checkSame(self, l.left, r.right) and checkSame(self, l.right, r.left)

        
        if root.left is None and root.right is None:
            return True

        elif root.left is None or root.right is None:
            return False

        return checkSame(self, root.left, root.right)




        