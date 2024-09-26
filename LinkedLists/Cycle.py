# Definition for singly-linked list.
from pyparsing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # setNodes = set()
        
        # curr = head

        # while curr is not None:

        #     if curr in setNodes:
        #         return True
        #     # Find a cycle

        #     setNodes.add(curr)
        #     curr = curr.next

        # return False

        slow = head
        fast = head

        while slow is not None and fast is not None:

            if slow.next is None or fast.next is None or fast.next.next is None:
                return False

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False