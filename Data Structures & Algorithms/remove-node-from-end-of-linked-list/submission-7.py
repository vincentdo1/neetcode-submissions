# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        to_return = head
        right_curr = head
        left_curr = head
        prev_curr = None
        for i in range(n):
            right_curr = right_curr.next
        while (right_curr != None):
            prev_curr = left_curr
            left_curr = left_curr.next
            right_curr = right_curr.next
        if (prev_curr == None):
            return head.next
        prev_curr.next = left_curr.next
        return to_return