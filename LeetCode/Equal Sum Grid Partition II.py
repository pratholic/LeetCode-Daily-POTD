from typing import DefaultDict, List


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        total_sum = sum(sum(row) for row in grid)

        bottom = DefaultDict(int)
        for i in range(m):
            for j in range(n):
                bottom[grid[i][j]] += 1


        top = DefaultDict(int)
        top_sum = 0

        for i in range(m - 1):
            for j in range(n):
                val = grid[i][j]
                top[val] += 1
                bottom[val] -= 1
                if bottom[val] == 0:
                    del bottom[val]

                top_sum += val

            bottom_sum = total_sum - top_sum

            if top_sum == bottom_sum:
                return True

            diff = abs(top_sum - bottom_sum)

            if top_sum > bottom_sum:
                larger_side = top
                rows = i + 1
                cols = n
                row_idx = i

            else:
                larger_side = bottom
                rows = m - (i + 1)
                cols = n
                row_idx = i + 1

            if rows > 1 and cols > 1:
                if diff in larger_side:
                    return True # kyuki yeh 2-d hai and connected bhi hoga hi

            else:
                if rows == 1: # col > 1 but row is single
                    r = row_idx
                    if larger_side is top:
                        if grid[r][0] == diff or grid[r][n - 1] == diff:
                            return True

                    else:
                        if grid[r][0] == diff or grid[r][n - 1] == diff:
                            return True

                else: # cols single hai
                    if larger_side is top:
                        if grid[0][0] == diff or grid[i][0] == diff:
                            return True

                    else:
                        if grid[i + 1][0] == diff or grid[m - 1][0] == diff:
                            return True

        
        right = DefaultDict(int)
        for i in range(m):
            for j in range(n):
                right[grid[i][j]] += 1

        left = DefaultDict(int)
        left_sum = 0

        for j in range(n - 1):
            for i in range(m):
                val = grid[i][j]
                left[val] += 1
                right[val] -= 1
                if right[val] == 0:
                    del right[val]

                left_sum += val

            right_sum = total_sum - left_sum

            if left_sum == right_sum:
                return True

            diff = abs(left_sum - right_sum)

            if left_sum > right_sum:
                larger_side = left
                rows = m
                cols = j + 1
                col_idx = j

            else:
                larger_side = right
                rows = m
                cols = n - (j + 1)
                col_idx = j + 1

            if rows > 1 and cols > 1:
                if diff in larger_side:
                    return True

            else: # 2-d wala case but in vertical cut case mein
                if cols == 1:
                    if larger_side is left:
                        if grid[0][col_idx] == diff or grid[m - 1][col_idx] == diff:
                            return True

                    else:
                        if grid[0][col_idx] == diff or grid[m - 1][col_idx] == diff:
                            return True


                else:
                    if larger_side is left:
                        if grid[0][0] == diff or grid[0][j] == diff:
                            return True
                    else:
                        if grid[0][j + 1] == diff or grid[0][n - 1] == diff:
                            return True

        return False