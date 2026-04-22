from collections import defaultdict
from typing import List


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] == x:
            return x

        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)

        if pu == pv:
            return

        if self.size[pu] < self.size[pv]:
            self.size[pv] += self.size[pu]
            self.parent[pu] = pv

        else:
            self.size[pu] += self.size[pv]
            self.parent[pv] = pu

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        dsu = DSU(n)

        for a, b in allowedSwaps:
            dsu.union(a, b)

        group_freq = defaultdict(lambda : defaultdict(int))

        for i in range(n):
            cur = source[i]
            parent = dsu.find(i)

            group_freq[parent][cur] += 1

        ans = 0
        for i in range(n):
            parent = dsu.find(i)

            if group_freq[parent][target[i]] > 0:
                group_freq[parent][target[i]] -= 1

            else:
                ans += 1

        return ans