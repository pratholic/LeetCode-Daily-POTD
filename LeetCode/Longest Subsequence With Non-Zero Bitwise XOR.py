from typing import List


class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)

        xr = 0

        for x in nums:
            xr ^= x

        if xr != 0:
            return n

        else:
            if all(x == 0 for x in nums):
                return 0

            else:
                return n - 1