# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        

        def getLength(self, head):
            if not head:
                return 0
            return 1 + getLength(self, head.next)

        length = getLength(self, head)


        # Index to remove at
        removeInd = length - n

        ghost = ListNode(0, next=head)

        prev = ghost

        curr = head

        # Add previous pointers

        for i in range(removeInd):
            prev = curr
            curr = curr.next
        
        # At the node to remove
        if curr.next:
            prev.next = curr.next
        else:
            prev.next = None
        
        return ghost.next