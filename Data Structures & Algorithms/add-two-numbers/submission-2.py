# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0)
        curr = res
        curr1, curr2 = l1, l2
        carry = 0
        while curr1 or curr2 or carry:
            curr1_val = curr1.val if curr1 else 0
            curr2_val = curr2.val if curr2 else 0
            sum_val = curr1_val + curr2_val + carry
            digit = sum_val % 10
            carry = sum_val // 10
            curr.next  = ListNode(digit)
            curr = curr.next
            curr1 = curr1.next if curr1 else None
            curr2 = curr2.next if curr2 else None
        return res.next