from typing import List
from math import gcd

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        
        dp = [[] for _ in range(16)]

        def f(idx, cur_lcm, cnt):
            if idx == n:
                dp[cnt].append(cur_lcm)
                return

            f(idx + 1, cur_lcm, cnt)

            if cur_lcm == 1:
                new_lcm = coins[idx]

            else:
                new_lcm = (cur_lcm * coins[idx]) // gcd(cur_lcm, coins[idx])

            f(idx + 1, new_lcm, cnt + 1)

        f(0, 1, 0)

        low = 1
        high = 10 ** 12

        ans = 0

        while low <= high:
            mid = (low + high) >> 1

            cnt = 0
            sign = 1

            for i in range(1, 16):
                for lcm in dp[i]:
                    if sign == 1:
                        cnt += (mid // lcm)

                    else:
                        cnt -= (mid // lcm)

                sign *= -1

            if cnt >= k:
                ans = mid
                high = mid - 1

            else:
                low = mid + 1

        return ans