from functools import cache
from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        suf = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suf[i] = suf[i + 1] + piles[i]

        @cache
        def f(idx, m):
            if idx >= n:
                return 0

            ans = 0

            for x in range(1, 2 * m + 1):
                new_i = idx + x
                new_m = max(m, x)

                cur = suf[idx] - f(new_i, new_m)

                ans = max(ans, cur)

            return ans

        return f(0, 1)