from typing import List
from collections import defaultdict

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)

        freq = defaultdict(int)
        l = 0
        ans = 0

        for r in range(n):
            freq[nums[r]] += 1

            while freq[nums[r]] > k:
                freq[nums[l]] -= 1
                l += 1

            ans = max(ans, r - l + 1)

        return ans