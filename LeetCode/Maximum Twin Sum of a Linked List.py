# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        vals = []
        tmp = head

        while tmp:
            vals.append(tmp.val)
            tmp = tmp.next

        ans = 0
        i, j = 0, len(vals) - 1

        while i < j:
            ans = max(ans, vals[i] + vals[j])
            i += 1
            j -= 1

        return ans