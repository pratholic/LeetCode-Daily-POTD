from typing import List


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)

        ans = 0

        for i in range(n):
            low, high = i, m - 1

            best = -1

            while low <= high:
                mid = (low + high) >> 1

                if nums2[mid] >= nums1[i]:
                    best = mid
                    low = mid + 1

                else:
                    high = mid - 1

            if best != -1:
                ans = max(ans, best - i)

        return ans