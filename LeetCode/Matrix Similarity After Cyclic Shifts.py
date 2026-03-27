from typing import List


class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m = len(mat)
        n = len(mat[0])
        new_mat = [row[:] for row in mat]

        for _ in range(k):
            for i in range(m):
                if i & 1:
                    cur_row = new_mat[i]
                    new_row = [cur_row[-1]] + cur_row[ : -1]
                    new_mat[i] = new_row

                else:
                    cur_row = new_mat[i]
                    new_row = cur_row[1:] + [cur_row[0]]
                    new_mat[i] = new_row

        return new_mat == mat