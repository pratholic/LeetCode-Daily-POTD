from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])

        ans = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:

                    # checking row that is there only one zero
                    cntz1 = 0
                    for col in range(n):
                        if col == j: continue
                        if mat[i][col] == 0:
                            cntz1 += 1

                    cntz2 = 0
                    for row in range(m):
                        if row == i: continue
                        if mat[row][j] == 0:
                            cntz2 += 1

                    if cntz1 == (n - 1) and cntz2 == (m - 1):
                        ans += 1

        return ans