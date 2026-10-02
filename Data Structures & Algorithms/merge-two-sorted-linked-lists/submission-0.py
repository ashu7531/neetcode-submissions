# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        res = ListNode(0, None)
        curr3 = res   
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                temp = curr1.next
                curr1.next = None
                curr3.next = curr1
                curr3 = curr3.next
                curr1 = temp
            else:
                temp = curr2.next
                curr2.next = None
                curr3.next = curr2
                curr3 = curr3.next
                curr2 = temp
        if not curr1:
            curr3.next = curr2
        if not curr2:
            curr3.next = curr1
        return res.next