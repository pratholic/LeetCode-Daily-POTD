from typing import List


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        col_sum = []
        row_sum = []

        for row in grid:
            row_sum.append(sum(row))

        for col in range(n):
            cur = 0
            for i in range(m):
                cur += grid[i][col]

            col_sum.append(cur)

        total_row_sum = sum(row_sum)
        total_col_sum = sum(col_sum)

        cur_row_sum = 0
        for i in range(len(row_sum)):
            if cur_row_sum == total_row_sum:
                return True

            cur_row_sum += row_sum[i]
            total_row_sum -= row_sum[i]

        cur_col_sum = 0
        for j in range(len(col_sum)):
            if cur_col_sum == total_col_sum:
                return True

            cur_col_sum += col_sum[j]
            total_col_sum -= col_sum[j]

        return False