from typing import List
from functools import cache

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)

        if not n & 1: # even case mein, p1 always wins
            return True

        @cache
        def f(i, j):
            if i == j:
                return nums[i]

            return max(nums[i] - f(i + 1, j), nums[j] - f(i, j - 1))

        return f(0, n - 1) >= 0