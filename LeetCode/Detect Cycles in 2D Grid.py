from collections import deque
from typing import List


class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        vis = [[False] * n for _ in range(m)]

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def valid(i, j):
            return i >= 0 and i < m and j >= 0 and j < n

        def bfs(sr, sc):
            q = deque()
            q.append((sr, sc, -1, -1))
            vis[sr][sc] = True

            while q:
                cr, cc, pr, pc = q.popleft()

                for dx, dy in dirs:
                    nr, nc = cr + dx, cc + dy

                    if not valid(nr, nc):
                        continue

                    if grid[nr][nc] != grid[cr][cc]:
                        continue

                    if nr == pr and nc == pc:
                        continue

                    if vis[nr][nc]:
                        return True

                    vis[nr][nc] = True
                    q.append((nr, nc, cr, cc))

            return False

        for i in range(m):
            for j in range(n):
                if not vis[i][j]:
                    if bfs(i, j):
                        return True

        return False