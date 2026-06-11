from typing import List


class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MOD = (10 ** 9) + 7

        n = len(edges) + 1

        tree = [[] for _ in range(n + 1)]

        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        max_depth = 0

        def dfs(node, parent, depth):
            nonlocal max_depth

            max_depth = max(max_depth, depth)

            for nei in tree[node]:
                if nei == parent:
                    continue

                dfs(nei, node, depth + 1)

        dfs(1, 0, 0)

        if max_depth == 0:
            return 0

        return pow(2, max_depth - 1, MOD)