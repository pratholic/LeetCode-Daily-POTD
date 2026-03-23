from typing import List


class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        MOD = (10 ** 9) + 7

        dp = {}

        def f(i, j):
            if i == m - 1 and j == n - 1:
                val = grid[i][j]
                return (val, val)

            state = (i, j)
            if state in dp:
                return dp[state]

            val = grid[i][j]
            lst = []

            if j + 1 < n:
                mx, mn = f(i, j + 1)
                lst.append(mx * val)
                lst.append(mn * val)

            
            if i + 1 < m:
                mx, mn = f(i + 1, j)
                lst.append(mx * val)
                lst.append(mn * val)

            dp[state] = (max(lst), min(lst))
            return dp[state]

        mx, _ = f(0, 0)
        return -1 if mx < 0 else mx % MOD