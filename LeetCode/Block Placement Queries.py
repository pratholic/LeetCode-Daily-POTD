from bisect import bisect_left, bisect_right
from typing import List

from sortedcontainers import SortedList


class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * self.n)

    def query(self, idx, l, r, start, end):
        if l > end or r < start:
            return 0

        if l >= start and r <= end:
            return self.tree[idx]

        mid = (l + r) >> 1

        return max(self.query(2 * idx + 1, l, mid, start, end), self.query(2 * idx + 2, mid + 1, r, start, end))

    def update(self, idx, l, r, u_val, u_idx):
        if l == r:
            self.tree[idx] = u_val
            return

        mid = (l + r) >> 1

        if u_idx <= mid:
            self.update(2 * idx + 1, l, mid, u_val, u_idx)

        else:
            self.update(2 * idx + 2, mid + 1, r, u_val, u_idx)

        self.tree[idx] = max(self.tree[2 * idx + 1], self.tree[2 * idx + 2])
        

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        MX = 50000

        seg = SegmentTree(MX + 1)

        obs = SortedList([0])

        ans = []

        for q in queries:
            if q[0] == 1:
                x = q[1]

                idx = bisect_left(obs, x)

                pred = obs[idx - 1]

                if idx < len(obs):
                    succ = obs[idx]

                    seg.update(0, 0, MX, succ - x, succ)

                seg.update(0, 0, MX, x - pred, x)

                obs.add(x)

            else:
                x = q[1]
                sz = q[2]

                idx = bisect_right(obs, x) - 1 # max obstacle <= x find kar rhe hai

                last = obs[idx]

                pref_max = seg.query(0, 0, MX, 0, last)

                best = max(pref_max, x - last)

                ans.append(best >= sz)

        return ans