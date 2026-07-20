from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        temp = grid

        for time in range(k):
            temp = [[0] * n for _ in range(m)]

            for i in range(m):

                for j in range(n):

                    ori = grid[i][j]

                    if i == m - 1 and j == n - 1:
                        temp[0][0] = ori

                    elif j == n - 1:
                        temp[i + 1][0] = ori

                    else:
                        temp[i][j + 1] = ori

            grid = temp

        return grid
                        
