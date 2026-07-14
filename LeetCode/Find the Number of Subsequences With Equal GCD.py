from typing import List
from math import gcd

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        n = len(nums)

        MOD = (10 ** 9) + 7

        dp = {}

        def f(idx, g1, g2):
            if idx == n:
                if g1 != 0 and g2 != 0 and g1 == g2:
                    return 1
                return 0

            state = (idx, g1, g2)

            if state in dp:
                return dp[state]

            x = nums[idx]

            take_seq1 = f(idx + 1, gcd(g1, x), g2)

            take_seq2 = f(idx + 1, g1, gcd(g2, x))

            not_take = f(idx + 1, g1, g2)

            dp[state] = (take_seq1 + take_seq2 + not_take) % MOD
            return dp[state]

        return f(0, 0, 0)