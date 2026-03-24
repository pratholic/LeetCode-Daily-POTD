from typing import List


class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        MOD = 12345

        arr = []
        for row in grid:
            arr.extend(row)

        k = len(arr)
        res = [1] * k

        pref = 1
        for i in range(k):
            res[i] = pref % MOD
            pref = (pref * arr[i]) % MOD

        suff = 1
        for i in range(k - 1, -1, -1):
            res[i] = (res[i] * suff) % MOD
            suff = (suff * arr[i]) % MOD

        ans = [[0] * m for _ in range(n)]
        idx = 0

        for i in range(n):
            for j in range(m):
                ans[i][j] = res[idx]
                idx += 1

        return ans