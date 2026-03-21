from typing import List


class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        sub_matrix = []

        for row in range(x, x + k):
            cur = []

            for col in range(y, y + k):
                cur.append(grid[row][col])

            sub_matrix.append(cur)

        sub_matrix.reverse()

        i = x
        for cur in sub_matrix:
            j = y

            for val in cur:
                grid[i][j] = val
                j += 1

            i += 1

        return grid