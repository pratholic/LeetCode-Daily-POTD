from typing import Counter, List


class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums)

        if n == 1:
            return False

        count = Counter(nums)

        for i in range(1, n):
            if i == n - 1:
                if count[i] != 2:
                    return False

            if i > 0 and i < n - 1:
                if count[i] != 1:
                    return False

        return True