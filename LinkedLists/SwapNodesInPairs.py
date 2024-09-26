# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head

        temp = ListNode()
        temp.next = head

        prev = temp

        while curr: 
            if curr.next and curr.next.next:
                ghost = curr.next
                prev.next = ghost
                curr.next = curr.next.next
                ghost.next = curr
                prev = curr

                curr = curr.next
            
            elif curr.next:
                prev.next = curr.next

                ghost = curr.next

                ghost.next = curr
                curr.next = None
                
                curr = curr.next

            # Last node in list
            else:
                curr = curr.next

            print(head)
            
        return temp.next