# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        


        ghost = ListNode(next=head)
        left = ghost

        curr = head
        prev = ghost

        while curr and curr.val < x:
            left = left.next
            curr = curr.next
            
        prev = left
        # Left at spot where next should be less
        # Curr at node to change
        
        while curr:

            # 5,4,3,2,5,2

            # prev = 3
            # Curr = 2
            # Left = ghost

            if curr.val < x:

                temp = curr

                curr = curr.next

                prev.next = temp.next

                temp.next = left.next

                left.next = temp

                left = temp

            # curr.val >=x
            else:
                prev = prev.next
                curr = curr.next
        

        return ghost.next