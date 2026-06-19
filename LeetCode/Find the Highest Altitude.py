from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)

        ans = [0]
        for i in range(n):
            ans.append(gain[i] + ans[-1])

        return max(ans)