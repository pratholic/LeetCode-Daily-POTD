from typing import List


class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        st = set(nums)

        mul = 1

        while k * mul in st:
            mul += 1

        return k * mul