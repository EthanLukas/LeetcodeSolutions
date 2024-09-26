# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def getLength(self, head):
            if not head:
                return 0
            return getLength(self, head.next) + 1


        if not head:
            return head
            
        numRotations = k% (getLength(self, head))
        
        # Each single rotation
        for rotation in range(numRotations):

            temp = head

            curr = head

            while curr.next.next:
                curr = curr.next
            
            ghost = curr.next

            ghost.next = temp

            curr.next = None

            head = ghost

        return head





