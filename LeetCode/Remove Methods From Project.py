from typing import List


class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        for u, v in invocations:
            g[u].append(v)

        vis = [False] * n

        def f(node):
            vis[node] = True

            for nei in g[node]:
                if not vis[nei]:
                    f(nei)

        f(k)

        for u, v in invocations:
            if not vis[u] and vis[v]:
                return list(range(n))

        ans = []
        for node in range(n):
            if not vis[node]:
                ans.append(node)

        return ans