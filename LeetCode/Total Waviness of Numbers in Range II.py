from functools import cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        
        def solve(x):

            digits = list(map(int, str(x)))
            n = len(digits)

            @cache
            def dfs(pos, started, tight, prev, trend, total):
                if pos == n:
                    return total # iss current number mein kitne waviness the

                limit = digits[pos] if tight else 9
                ans = 0

                for d in range(limit + 1):

                    new_tight = tight and (d == limit)

                    if not started and d == 0:
                        ans += dfs(pos + 1, False, new_tight, 0, 0, total)

                    elif not started: # but d > 0, so non-zero digit aagya
                        ans += dfs(pos + 1, True, new_tight, d, 0, total)

                    else:
                        if d > prev:
                            new_trend = 2

                            add = 1 if trend == 1 else 0

                        elif d < prev:
                            new_trend = 1

                            add = 1 if trend == 2 else 0

                        else:
                            new_trend = 0
                            add = 0

                        ans += dfs(pos + 1, True, new_tight, d, new_trend, total + add)

                return ans

            return dfs(0, False, True, 0, 0, 0)

        return solve(num2) - solve(num1 - 1)