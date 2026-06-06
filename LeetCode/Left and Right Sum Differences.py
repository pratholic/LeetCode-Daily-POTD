from typing import List


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []

        pref = [0] * n
        suf = [0] * n

        for i in range(1, n):
            pref[i] = nums[i - 1] + pref[i - 1]

        for i in range(n - 2, -1, -1):
            suf[i] = nums[i + 1] + suf[i + 1]

        for i in range(n):
            left = pref[i]
            right = suf[i]

            ans.append(abs(left - right))

        return ans