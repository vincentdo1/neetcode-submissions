# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        to_return = head
        prev = None
        curr = head
        length = 0
        while (curr != None):
            length += 1
            curr = curr.next
        curr = head
        if (length - n == 0):
            return head.next
        for i in range(0, length - n):
            prev = curr
            curr = curr.next
        if (curr != None):
            prev.next = curr.next
        else:
            prev.next = None
        return to_return