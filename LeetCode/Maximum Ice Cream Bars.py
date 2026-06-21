from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        n = len(costs)

        if min(costs) > coins:
            return 0

        costs.sort()

        ans = 0

        for i, bar in enumerate(costs):
            if bar <= coins:
                coins -= bar
                ans += 1

            else:
                break

        return ans