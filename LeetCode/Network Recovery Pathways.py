from collections import deque
from typing import List


class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online) # taking length of online coz we can only use these nodes which are online
        graph = [[] for _ in range(n)]

        indegree = [0] * n

        for u, v, cost in edges:
            if online[u] and online[v]:
                graph[u].append((v, cost))
                indegree[v] += 1

        q = deque()
        topo = []

        for node in range(n):
            if indegree[node] == 0 and online[node]:
                q.append(node)

        while q:
            cur = q.popleft()

            topo.append(cur)

            for v, cost in graph[cur]:
                indegree[v] -= 1

                if indegree[v] == 0:
                    q.append(v)

        def check(mid):
            dist = [float('inf')] * n
            dist[0] = 0

            for node in topo:
                if dist[node] == float('inf'):
                    continue
                
                for v, cost in graph[node]:
                    if cost >= mid:
                        dist[v] = min(dist[v], dist[node] + cost)

            return dist[n - 1] <= k

        low = 0
        high = k
        ans = -1

        while low <= high:
            mid = (low + high) >> 1

            if check(mid):
                ans = mid
                low = mid + 1

            else:
                high = mid - 1

        return ans