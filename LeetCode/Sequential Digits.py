from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        s = "123456789"

        for sz in range(2, 10):
            for start in range(10 - sz):
                num = int(s[start : start + sz])

                if low <= num <= high:
                    ans.append(num)

        return ans