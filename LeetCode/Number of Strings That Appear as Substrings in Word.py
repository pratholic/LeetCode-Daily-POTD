from typing import List


class Solution:
    def numOfStrings(self, patterns: List[str], w: str) -> int:
        ans = 0

        for word in patterns:
            if word in w:
                ans += 1

        return ans