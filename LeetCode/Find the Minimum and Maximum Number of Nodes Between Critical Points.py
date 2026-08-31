# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        nodes = []

        def f(node):
            if not node:
                return

            nodes.append(node.val)
            f(node.next)

        f(head)

        if len(nodes) < 3:
            return [-1, -1]

        locals = []

        for i in range(1, len(nodes) - 1):
            if (nodes[i - 1] < nodes[i] > nodes[i + 1]) or (nodes[i - 1] > nodes[i] < nodes[i + 1]):
                locals.append(i)

        if len(locals) < 2:
            return [-1, -1]

        mn = float('inf')
        for i in range(1, len(locals)):
            mn = min(mn, locals[i] - locals[i - 1])

        mx = locals[-1] - locals[0]
        return [mn, mx]