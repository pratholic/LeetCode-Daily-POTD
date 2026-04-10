from typing import List


class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)

        ans = float('inf')

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i != j and i != k and j != k and nums[i] == nums[j] == nums[k]:
                        dist = abs(i - j) + abs(j - k) + abs(k - i)
                        ans = min(ans, dist)

        return ans if ans != float('inf') else -1