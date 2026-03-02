from typing import List


class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        trailing = []

        for row in grid:
            count = 0

            for x in reversed(row):
                if x == 0:
                    count += 1

                else:
                    break

            trailing.append(count)

        swaps = 0
        for i in range(n):
            need = n - i - 1 # itne zeros chahiye yaha pe to satisfy the above wala condition

            j = i
            while j < n and trailing[j] < need:
                j += 1 # cur row se find karo ki niche esi trailing zeros wali row hai ki nahi

            if j == n:
                return -1 # if nahi mili, return -1

            while j > i:
                trailing[j], trailing[j - 1] = trailing[j - 1], trailing[j]
                j -= 1
                swaps += 1

        return swaps