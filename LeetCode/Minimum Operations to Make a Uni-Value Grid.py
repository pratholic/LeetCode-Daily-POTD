from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        m = len(grid)
        n = len(grid[0])

        base = grid[0][0] % x
        for i in range(m):
            for j in range(n):
                if grid[i][j] % x != base:
                    return -1


        nums = sorted([val for row in grid for val in row])

        total = sum(nums)
        pref = 0
        ans = float('inf')

        for i in range(len(nums)):
            left = nums[i] * i - pref
            right = (total - pref) - (nums[i] * (len(nums) - i))
            cost = (left + right) // x

            ans = min(ans, cost)
            pref += nums[i]

        return ans