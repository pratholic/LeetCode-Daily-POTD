from typing import List


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def findUPar(self, node):
        if node == self.parent[node]:
            return node

        self.parent[node] = self.findUPar(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        pu = self.findUPar(u)
        pv = self.findUPar(v)

        if pu == pv:
            return

        if self.size[pu] < self.size[pv]:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]

        else:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        
        dsu = DSU(n)

        ans = []

        for i in range(1, n):
            if nums[i] - nums[i - 1] <= maxDiff:
                dsu.union(i, i - 1)

        for u, v in queries:
            if dsu.findUPar(u) == dsu.findUPar(v):
                ans.append(True)

            else:
                ans.append(False)

        return ans