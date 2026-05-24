from typing import List


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)

        dp = [-1] * n

        def f(idx):

            if dp[idx] != -1:
                return dp[idx]

            steps = 1

            for x in range(1, d + 1):
                j = idx + x

                if j >= n or arr[j] >= arr[idx]:
                    break

                steps = max(steps, 1 + f(j))

            for x in range(1, d + 1):
                j = idx - x

                if j < 0 or arr[j] >= arr[idx]:
                    break

                steps = max(steps, 1 + f(j))

            dp[idx] = steps
            return dp[idx]

        ans = 0
        for i in range(n):
            ans = max(ans, f(i))

        return ans