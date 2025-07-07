from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head and not head.next:
            return None

        curr = head
        size = 0
        while curr:
            size += 1
            curr = curr.next

        cnt = 0
        d = ListNode()
        curr = head
        prev = None
        d.next = curr

        print(size)

        while curr:
            if cnt == size - n:
                if prev is None:
                    return curr.next

                prev.next = curr.next
                break

            prev = curr
            curr = curr.next

            cnt += 1

        return d.next

