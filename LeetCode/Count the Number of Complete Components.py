from collections import deque
from typing import List


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]

        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        vis = [False] * n
        ans = 0

        for node in range(n):
            if vis[node]:
                continue

            q = deque()
            q.append(node)
            nodes = 0
            deg = 0
            vis[node] = True

            while q:
                cur = q.popleft()
                deg += len(g[cur]) # edges count karli from cur
                nodes += 1

                for nei in g[cur]:
                    if not vis[nei]:
                        q.append(nei)
                        vis[nei] = True

            edge_cnt = deg // 2
            if edge_cnt == nodes * (nodes - 1) // 2:
                ans += 1

        return ans