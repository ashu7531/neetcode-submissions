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
        while curr1 and curr2:
            sum_val = curr1.val + curr2.val + carry
            digit = sum_val % 10
            carry = sum_val // 10
            curr.next  = ListNode(digit)
            curr = curr.next
            curr1 = curr1.next
            curr2 = curr2.next
        while curr1:
            sum_val = curr1.val + carry
            digit = sum_val % 10
            carry = sum_val // 10
            curr.next  = ListNode(digit)
            curr = curr.next
            curr1 = curr1.next
        while curr2:
            sum_val = curr2.val + carry
            digit = sum_val % 10
            carry = sum_val // 10
            curr.next  = ListNode(digit)
            curr = curr.next
            curr2 = curr2.next
        while carry > 0:
            digit = carry % 10
            carry = carry // 10
            curr.next  = ListNode(digit)
            curr = curr.next
        return res.next