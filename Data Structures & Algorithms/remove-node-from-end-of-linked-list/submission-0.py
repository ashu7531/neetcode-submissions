# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = ListNode(0, head)
        pointer1 = curr
        last = head
        while n > 0:
            last = last.next
            n -= 1
        while last:
            last = last.next
            pointer1 = pointer1.next
        pointer1.next = pointer1.next.next
        return curr.next