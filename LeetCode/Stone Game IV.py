from math import sqrt


class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        
        dp = {}

        def f(stones, turn):
            if stones == 0:
                return False

            if (stones, turn) in dp:
                return dp[(stones, turn)]

            for k in range(1, sqrt(stones) + 1):
                sq = k * k

                if not f(stones - sq, 1 ^ turn):
                    dp[(stones, turn)] = True
                    return True

            dp[(stones, turn)] = False
            return False

        ans = f(n, 0)
        return dp[(n, 0)]