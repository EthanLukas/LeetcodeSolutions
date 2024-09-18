# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    
        carry = 0

        combined = l1.val + l2.val

        # Carry over a 1
        if combined >= 10:
            carry += 1 

        if carry > 0:
            result = ListNode(combined-10)
        # carry is 0
        else:
            result = ListNode(combined)

        current = result

        l1 = l1.next
        l2 = l2.next

        # Both exist still
        while l1 is not None and l2 is not None:

            combined = l1.val + l2.val + carry
            carry = 0

            if combined >= 10:
                carry += 1
            
            if carry > 0:
                current.next = ListNode(combined-10)
                current = current.next
            # No carry
            else:
                current.next = ListNode(combined)
                current = current.next
        
            l1 = l1.next
            l2 = l2.next
        
        # Only one list remains
        while l1 is not None:
            combined = l1.val + carry
            carry = 0

            if combined >= 10:
                carry += 1
            
            if carry > 0:
                current.next = ListNode(combined-10)
                current = current.next
            # No carry
            else:
                current.next = ListNode(combined)
                current = current.next

            l1 = l1.next

        while l2 is not None:
            combined = l2.val + carry
            carry = 0

            if combined >= 10:
                carry += 1
            
            if carry > 0:
                current.next = ListNode(combined-10)
                current = current.next
            # No carry
            else:
                current.next = ListNode(combined)
                current = current.next

            l2 = l2.next

        if carry > 0:
            current.next = ListNode(carry)

        return result