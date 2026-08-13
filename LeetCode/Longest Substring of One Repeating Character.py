from typing import List


class Solution:
    class Node:
        def __init__(self, pref = 0, suf = 0, mx_len = 0, left = None, right = None):
            self.pref = pref
            self.suf = suf
            self.mx_len = mx_len
            self.left = left
            self.right = right


    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        ans = []
        tree = [None] * (4 * n)

        def merge(left_node, right_node, left_len, right_len):
            node = self.Node()

            node.left = left_node.left
            node.right = right_node.right

            node.pref = left_node.pref
            if left_node.pref == left_len and left_node.right == right_node.left:
                node.pref = left_node.pref + right_node.pref

            node.suf = right_node.suf
            if right_node.suf == right_len and right_node.left == left_node.right:
                node.suf = right_node.suf + left_node.suf

            node.mx_len = max(left_node.mx_len, right_node.mx_len)

            if left_node.right == right_node.left:
                node.mx_len = max(node.mx_len, left_node.suf + right_node.pref)

            return node


        def build(idx, l, r):
            if l == r:
                tree[idx] = self.Node(1, 1, 1, s[l], s[l])
                return

            mid = (l + r) >> 1

            build(2 * idx + 1, l, mid)
            build(2 * idx + 2, mid + 1, r)

            tree[idx] = merge(tree[2 * idx + 1], tree[2 * idx + 2], mid - l + 1, r - mid)

        
        def update(idx, l, r, u_pos, u_val):
            if l == r:
                tree[idx] = self.Node(1, 1, 1, u_val, u_val)
                return

            mid = (l + r) >> 1

            if u_pos <= mid:
                update(2 * idx + 1, l, mid, u_pos, u_val)

            else:
                update(2 * idx + 2, mid + 1, r, u_pos, u_val)

            tree[idx] = merge(tree[2 * idx + 1], tree[2 * idx + 2], mid - l + 1, r - mid)

        build(0, 0, n - 1)

        for ch, pos in zip(queryCharacters, queryIndices):
            update(0, 0, n - 1, pos, ch)
            ans.append(tree[0].mx_len)

        return ans