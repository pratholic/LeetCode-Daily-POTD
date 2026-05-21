from typing import List


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        seen = set()

        for num in arr1:
            while num > 0:
                seen.add(num)
                num //= 10

        ans = 0

        for num in arr2:

            while num > 0:

                if num in seen:
                    ans = max(ans, len(str(num)))
                    break

                num //= 10

        return ans