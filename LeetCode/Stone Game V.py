from typing import List
from functools import lru_cache

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)

        pref = [0] * (n)
        pref[0] = stoneValue[0]
        for i in range(1, n):
            pref[i] = pref[i - 1] + stoneValue[i]

        def get(i, j):
            if i == 0:
                return pref[j]

            return pref[j] - pref[i - 1]

        @lru_cache(None)
        def f(i, j):
            if i == j:
                return 0

            res = 0

            for k in range(i, j):
                left = get(i, k)
                right = get(k + 1, j)

                if 2 * min(left, right) > res:
                    if left <= right:
                        res = max(res, f(i, k) + left)

                    if left >= right:
                        res = max(res, f(k + 1, j) + right)

            return res

        return f(0, n - 1)