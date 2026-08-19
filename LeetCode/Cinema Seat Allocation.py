from typing import List


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows = {}

        for r, s in reservedSeats:
            rows.setdefault(r, set()).add(s)

        ans = (n - len(rows)) * 2

        for seats in rows.values():
            left = all(s not in seats for s in [2, 3, 4, 5])
            mid = all(s not in seats for s in [4, 5, 6, 7])
            right = all(s not in seats for s in [6, 7, 8, 9])

            if left and right:
                ans += 2

            elif mid or left or right:
                ans += 1

        return ans