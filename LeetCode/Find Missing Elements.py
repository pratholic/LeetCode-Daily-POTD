from typing import Counter, List


class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        start, end = min(nums), max(nums)

        ans = []

        f = Counter(nums)

        while start < end:
            if start not in f:
                ans.append(start)

            else:
                pass

            start += 1

        return ans