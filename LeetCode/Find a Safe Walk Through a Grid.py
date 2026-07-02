from typing import List


class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m = len(grid)
        n = len(grid[0])

        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def isValid(i, j):
            return i >= 0 and i < m and j >= 0 and j < n

        dp = {}
        visited = set()

        def f(i, j, rem):
            rem -= grid[i][j]

            if rem <= 0:
                return False

            if i == m - 1 and j == n - 1:
                return rem > 0

            if (i, j, rem) in dp:
                return dp[(i, j, rem)]

            visited.add((i, j))

            for dx, dy in dirs:
                ni, nj = i + dx, j + dy

                if isValid(ni, nj) and (ni, nj) not in visited:
                    if f(ni, nj, rem):
                        visited.remove((i, j))
                        dp[(i, j, rem)] = True
                        return True

            visited.remove((i, j))
            dp[(i, j, rem)] = False
            return False

        return f(0, 0, health)