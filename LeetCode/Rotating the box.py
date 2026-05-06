from typing import List


class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m, n = len(boxGrid), len(boxGrid[0])

        ans = [[''] * m for _ in range(n)]

        for i in range(m):
            for j in range(n):
                ans[j][m - i - 1] = boxGrid[i][j]

        rows = n
        cols = m

        for col in range(m):
            write = rows - 1

            for row in range(rows - 1, -1, -1):
                if ans[row][col] == '*':
                    write = row - 1 # stones iske upar hi aayenge

                elif ans[row][col] == '#':
                    ans[row][col] = '.'
                    ans[write][col] = '#'

                    write -= 1

        return ans