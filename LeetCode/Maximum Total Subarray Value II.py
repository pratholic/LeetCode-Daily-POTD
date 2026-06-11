from heapq import heappop, heappush
from typing import List


class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [(-float('inf'), float('inf'))] * (4 * self.n) # each node stores (max, min)
        self.build(0, 0, self.n - 1, nums)

    def merge(self, left, right):
        return (max(left[0], right[0]), min(left[1], right[1]))

    def build(self, idx, l, r, nums):
        if l == r:
            self.tree[idx] = (nums[l], nums[l])
            return

        mid = (l + r) >> 1
        self.build(2 * idx + 1, l, mid, nums)
        self.build(2 * idx + 2, mid + 1, r, nums)

        self.tree[idx] = self.merge(self.tree[2 * idx + 1], self.tree[2 * idx + 2])

    def query(self, ql, qr):
        # internal self made query() chalao and [0..n-1] ki range se start karke [ql...qr] ki values le aao
        return self._query(0, 0, self.n - 1, ql, qr)

    def _query(self, idx, l, r, ql, qr):
        if l > qr or r < ql:
            return (-float('inf'), float('inf'))

        if l >= ql and r <= qr:
            return self.tree[idx]

        mid = (l + r) >> 1

        left = self._query(2 * idx + 1, l, mid, ql, qr)
        right = self._query(2 * idx + 2, mid + 1, r, ql, qr)

        return self.merge(left, right)

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)

        seg = SegmentTree(nums)

        vis = {(0, n - 1)}
        pq = []

        mx, mn = seg.query(0, n - 1)
        heappush(pq, (-(mx - mn), 0, n - 1))

        ans = 0

        while pq and k:
            neg_val, l, r = heappop(pq)
            val = -neg_val

            ans += val
            k -= 1

            if l + 1 <= r and (l + 1, r) not in vis:
                mx, mn = seg.query(l + 1, r)
                heappush(pq, (-(mx - mn), l + 1, r))
                vis.add((l + 1, r))

            if r - 1 >= l and (l, r - 1) not in vis:
                mx, mn = seg.query(l, r - 1)
                heappush(pq, (-(mx - mn), l, r - 1))
                vis.add((l, r - 1))

        return ans