class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        pref = [0] * n
        pref[0] = nums[0]

        for i in range(1, n):
            pref[i] = max(pref[i - 1], nums[i])

        suf = [0] * n
        suf[-1] = nums[-1]

        for i in range(n - 2, -1, -1):
            suf[i] = min(suf[i + 1], nums[i])

        for i in range(n):
            if pref[i] - suf[i] <= k:
                return i

        return -1