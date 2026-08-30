from typing import List


class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        mn = min(nums)
        mx = max(nums)

        mn_idx = nums.index(mn)
        mx_idx = nums.index(mx)

        left = min(mn_idx, mx_idx)
        right = max(mx_idx, mn_idx)

        front = right + 1

        back = n - left

        mixed = (left + 1) + (n - right)

        return min(front, back, mixed)