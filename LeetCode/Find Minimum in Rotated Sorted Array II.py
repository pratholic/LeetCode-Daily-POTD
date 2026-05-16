from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        a = []
        vis = set()

        for x in nums:
            if (not a or a[-1] != x) and x not in vis:
                a.append(x)
                vis.add(x)


        low, high = 0, len(a) - 1
        ans = 10 ** 18

        while low <= high:
            mid = (low + high) >> 1

            ans = min(ans, a[mid])

            if a[mid] < a[high]:
                high = mid - 1

            else:
                low = mid + 1

        return ans