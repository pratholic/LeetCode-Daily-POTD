from math import sqrt
from typing import List

class Solution:
    def minNumberOfSeconds(self, mH: int, workerTimes: List[int]) -> int:
        n = len(workerTimes)

        def check(t):
            h = 0
            for val in workerTimes:
                h += int(sqrt(((2.0 * t) / val) + 0.25) - 0.5)

                if h >= mH:
                    return True

            return h >= mH

        low = 1
        high = max(workerTimes) * (mH * (mH + 1) // 2)
        ans = high

        while low <= high:
            mid = (low + high) >> 1

            if check(mid):
                ans = mid
                high = mid - 1

            else:
                low = mid + 1

        return ans