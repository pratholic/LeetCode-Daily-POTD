from typing import List


class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        NEG = -10 ** 9

        dp = [-1] * n

        def f(idx):
            if idx == n - 1:
                return 0

            if dp[idx] != -1:
                return dp[idx]

            jump = NEG
            for j in range(idx + 1, n):
                if -target <= nums[j] - nums[idx] <= target:
                    nxt = f(j)

                    if nxt != NEG:
                        jump = max(jump, 1 + nxt)

            dp[idx] = jump
            return dp[idx]

        ans = f(0)
        return ans if ans != NEG else -1