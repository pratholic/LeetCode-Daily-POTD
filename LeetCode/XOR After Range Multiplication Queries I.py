from typing import List


class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        MOD = (10 ** 9) + 7

        for l, r, k, v in queries:

            idx = l

            while idx <= r:
                nums[idx] *= v
                nums[idx] %= MOD

                idx += k

        xr = 0
        for i in nums:
            xr ^= i

        return xr