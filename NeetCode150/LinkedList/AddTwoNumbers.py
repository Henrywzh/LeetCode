from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        total = 0
        d = ListNode()
        curr = d

        while l1 and l2:
            total = l1.val + l2.val + carry
            print(total)
            carry = total // 10
            l1, l2 = l1.next, l2.next
            curr.next = ListNode(total % 10)
            curr = curr.next

        while l1:
            total = l1.val + carry
            carry = total // 10
            l1 = l1.next
            curr.next = ListNode(total % 10)
            curr = curr.next

        while l2:
            total = l2.val + carry
            carry = total // 10
            l2 = l2.next
            curr.next = ListNode(total % 10)
            curr = curr.next

        if total // 10 > 0:
            curr.next = ListNode(1)

        return d.next
