from typing import List


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] != 0:
                    matrix[i][j] += matrix[i - 1][j]

        mx = 0
        
        for row in matrix:
            row.sort(reverse = True)

            for j in range(n):
                mx = max(mx, row[j] * (j + 1))

        return mx