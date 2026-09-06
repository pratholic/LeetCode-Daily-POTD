class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)

        dp = {}

        def f(i, j):
            if j == m:
                return 1

            if i == n:
                return 0

            if (i, j) in dp:
                return dp[(i, j)]

            ans = f(i + 1, j)

            if s[i] == t[j]:
                ans += f(i + 1, j + 1)

            dp[(i, j)] = ans
            return ans

        return f(0, 0)