# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tort = head
        hare = head
        if (head == None or head.next == None):
            return False
        while (tort != None and hare != None):
            tort = tort.next
            hare = hare.next
            if (hare != None):
                hare = hare.next
            if (tort == hare):
                return True
        return False