from collections import deque
from typing import List


class Solution:
    def minMoves(self, grid: List[str], energy: int) -> int:
        m, n = len(grid), len(grid[0])
        start = None
        litter = []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'S': # start mil gaya
                    start = (i, j)

                elif grid[i][j] == 'L':
                    litter.append((i, j))

        def valid(i, j):
            return i >= 0 and i < m and j >= 0 and j < n and grid[i][j] != 'X'

        k = len(litter)
        litter_id = {}

        for i, (r, c) in enumerate(litter):
            litter_id[(r, c)] = i

        full = (1 << k) - 1

        q = deque()
        q.append((start[0], start[1], 0, energy, 0)) # (row, col, litter collected, energy, steps)

        best = [[[-1] * (1 << k) for _ in range(n)] for _ in range(m)]
        best[start[0]][start[1]][0] = energy

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while q:
            r, c, mask, rem_energy, steps = q.popleft()

            if mask == full:
                return steps

            if rem_energy == 0:
                continue

            for dx, dy in dirs:
                nrow, ncol = dx + r, dy + c

                if valid(nrow, ncol):
                    new_mask = mask
                    new_energy = rem_energy - 1

                    if (nrow, ncol) in litter_id:
                        idx = litter_id[(nrow, ncol)]
                        new_mask = mask | (1 << idx)

                    if grid[nrow][ncol] == 'R':
                        new_energy = energy

                    if best[nrow][ncol][new_mask] >= new_energy:
                        continue # already zyada energy leke bethe hai, type of pruning

                    best[nrow][ncol][new_mask] = new_energy

                    q.append((nrow, ncol, new_mask, new_energy, steps + 1))

        return -1