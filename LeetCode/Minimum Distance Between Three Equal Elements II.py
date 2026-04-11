from typing import DefaultDict, List


class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        mp = DefaultDict(list)

        for i,x in enumerate(nums):
            mp[x].append(i)

        ans = float('inf')
        for indices in mp.values():
            if len(indices) < 3:
                continue

            for i in range(len(indices) - 2):
                ans = min(ans, 2 * (indices[i + 2] - indices[i]))

        return ans if ans != float('inf') else -1