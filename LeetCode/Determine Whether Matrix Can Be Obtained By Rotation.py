from typing import List


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)

        def rotate(grid):
            for i in range(n):
                for j in range(i, n):
                    grid[i][j], grid[j][i] = grid[j][i], grid[i][j]

            for row in grid:
                row.reverse()

        for c in range(4):
            equal = True

            for i in range(n):
                for j in range(n):
                    if mat[i][j] != target[i][j]:
                        equal = False
                        break

            if equal:
                return True

            rotate(mat)

        return False