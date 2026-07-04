from typing import DefaultDict, Deque, List


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = DefaultDict(list)

        for u, v, wt in roads:
            graph[u].append((v, wt))
            graph[v].append((u, wt))

        vis = [False] * (n + 1)
        vis[1] = True

        q = Deque([1])
        ans = float('inf')

        while q:
            node = q.popleft()

            for nei, wt in graph[node]:
                ans = min(ans, wt)

                if not vis[nei]:
                    vis[nei] = True
                    q.append(nei)

        return ans