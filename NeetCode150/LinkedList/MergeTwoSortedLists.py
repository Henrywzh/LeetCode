from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        d = ListNode()
        curr = d
        h1, h2 = list1, list2

        while h1 and h2:
            if h1.val < h2.val:
                curr.next = ListNode(h1.val)
                h1 = h1.next
            else:
                curr.next = ListNode(h2.val)
                h2 = h2.next
            curr = curr.next

        while h1:
            curr.next = ListNode(h1.val)
            h1 = h1.next
            curr = curr.next

        while h2:
            curr.next = ListNode(h2.val)
            h2 = h2.next
            curr = curr.next

        return d.next
    