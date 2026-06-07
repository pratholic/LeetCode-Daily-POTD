# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        childs = set()

        for p, c, left in descriptions:
            if p not in nodes:
                nodes[p] = TreeNode(p)

            if c not in nodes:
                nodes[c] = TreeNode(c)

            if left == 1:
                nodes[p].left = nodes[c]

            else:
                nodes[p].right = nodes[c]

            childs.add(c)

        for p, _, _ in descriptions:
            if p not in childs:
                return nodes[p]