from typing import Deque, List


class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        dirs = {
            1 : [(0, -1), (0, 1)],
            2 : [(-1, 0), (1, 0)],
            3 : [(0, -1), (1, 0)],  
            4 : [(0, 1), (1, 0)],
            5 : [(0, -1), (-1, 0)],  
            6 : [(0, 1), (-1, 0)]
        }

        def isValid(i, j):
            return i >= 0 and i < m and j >= 0 and j < n

        vis = [[False] * n for _ in range(m)]
        vis[0][0] = True

        q = Deque()
        q.append((0, 0))

        while q:
            r, c = q.popleft()
            if r == m - 1 and c == n - 1:
                return True

            val = grid[r][c]
            cells = dirs[val]

            for dx, dy in cells:
                nr, nc = dx + r, dy + c

                if isValid(nr, nc) and not vis[nr][nc]:

                    for odx, ody in dirs[grid[nr][nc]]:
                        if (odx + nr == r) and (ody + nc == c):
                            q.append((nr, nc))
                            vis[nr][nc] = True

        return False