# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:

        cur = []
        ans = [0]

        def to_decimal(lst):
            val = 0
            lst = lst[::-1]
            for i, v in enumerate(lst):
                if v == 1:
                    val += (1 << i)

            return val

        def isLeaf(node):
            return node and not node.left and not node.right 

        def f(node):

            cur.append(node.val)
            if isLeaf(node):
                ans[0] += to_decimal(cur)

            else:
                if node.left: f(node.left)
                if node.right: f(node.right)

            cur.pop()

        f(root)
        return ans[0]