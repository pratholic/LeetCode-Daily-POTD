from typing import List


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)

        total = sum(nums)
        f = 0
        for i, num in enumerate(nums):
            f += i * num
        mx = f

        for k in range(n):
            new_f = f + total - n * nums[n - 1 - k]
            mx = max(mx, new_f)
            f = new_f

        return mx