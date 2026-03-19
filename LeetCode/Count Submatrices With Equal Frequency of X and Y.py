from typing import List


class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])

        pref = [[0] * m for i in range(n)]
        count_x = [[0] * m for i in range(n)]

        for i in range(n):
            for j in range(m):
                val = 0

                if grid[i][j] == 'X':
                    val = 1

                elif grid[i][j] == 'Y':
                    val = -1

                x = 1 if val == 1 else 0

                pref[i][j] = val
                count_x[i][j] = x

                if i > 0:
                    pref[i][j] += pref[i - 1][j]
                    count_x[i][j] += count_x[i - 1][j]

                if j > 0:
                    pref[i][j] += pref[i][j - 1]
                    count_x[i][j] += count_x[i][j - 1]

                if i > 0 and j > 0:
                    pref[i][j] -= pref[i - 1][j - 1]
                    count_x[i][j] -= count_x[i - 1][j - 1]

        
        ans = 0
        for i in range(n):
            for j in range(m):
                if pref[i][j] == 0 and count_x[i][j] > 0:
                    ans += 1

        return ans