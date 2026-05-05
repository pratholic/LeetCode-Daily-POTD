# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or not head.next or k == 0:
            return head
        
        def size(root):
            tmp = root
            cnt = 0
            while tmp:
                cnt += 1
                tmp = tmp.next

            return cnt

        
        n = size(head)
        k %= n

        if k == 0:
            return head

        a = []
        tmp = head

        while tmp:
            a.append(tmp.val)
            tmp = tmp.next

        a = a[-k:] + a[:-k]

        tmp = head
        i = 0
        while tmp:
            tmp.val = a[i]
            i += 1
            tmp = tmp.next

        return head