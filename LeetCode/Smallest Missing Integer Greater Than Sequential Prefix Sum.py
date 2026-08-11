from typing import List


class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n = len(nums)

        st = set(nums)
        pref = nums[0]

        for i in range(1, n):
            if nums[i] == nums[i - 1] + 1:
                pref += nums[i]

            else: break

        while pref in st:
            pref += 1

        return pref