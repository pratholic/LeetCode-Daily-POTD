class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m = len(coins)
        n = len(coins[0])

        dp = [[[None] * 3 for _ in range(n)] for _ in range(m)]

        def f(i, j, ability):
            if i >= m or j >= n:
                return float('-inf')


            if dp[i][j][ability] is not None:
                return dp[i][j][ability]

            
            val = coins[i][j]

            if i == m - 1 and j == n - 1:
                if val >= 0:
                    dp[i][j][ability] = val

                else:
                    if ability > 0:
                        dp[i][j][ability] = 0

                    else:
                        dp[i][j][ability] = val

                return dp[i][j][ability]


            nxt_best = max(f(i + 1, j, ability), f(i, j + 1, ability))

            if val >= 0:
                ans = val + nxt_best

            else:
                with_loss = val + nxt_best # jab we don't have ability

                neutral = float('-inf')
                if ability > 0:
                    neutral = max(f(i + 1, j, ability - 1), f(i, j + 1, ability - 1))

                ans = max(with_loss, neutral)

            dp[i][j][ability] = ans
            return ans

        return f(0, 0, 2)