from typing import List


class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]

        for i in range(m - k + 1):
            for j in range(n - k + 1):
                s = set()

                for x in range(i, i + k):
                    for y in range(j, j + k):
                        s.add(grid[x][y])

                arr = sorted(s)

                mn = float('inf')
                for e in range(1, len(arr)):
                    mn = min(mn, arr[e] - arr[e - 1])

                if mn != float('inf'):
                    ans[i][j] = mn

        return ans