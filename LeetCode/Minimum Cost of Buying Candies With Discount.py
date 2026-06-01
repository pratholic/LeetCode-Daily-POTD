from typing import List


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        n = len(cost)
        cost.sort()
        ans = 0

        if n == 1:
            return cost[0]

        elif n == 2 or n == 3:
            return cost[-1] + cost[-2]

        stack = []
        for i in range(n - 1, -1, -1):
            if not stack or len(stack) < 2:
                stack.append(cost[i])
                ans += cost[i]

            else:
                stack.clear()

        return ans