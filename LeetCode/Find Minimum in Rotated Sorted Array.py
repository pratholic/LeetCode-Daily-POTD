from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        low, high = 0, n - 1
        ans = nums[0]

        while low <= high:
            mid = (low + high) >> 1

            ans = min(ans, nums[mid])

            if nums[mid] < nums[high]:
                high = mid - 1

            else:
                low = mid + 1

        return ans