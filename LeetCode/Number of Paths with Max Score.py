from typing import List
from functools import cache

class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        m = len(board)
        MOD = (10 ** 9) + 7

        NEG = -float('inf')

        dirs = [(-1, 0), (0, -1), (-1, -1)]
        
        @cache
        def f(i, j):
            if i < 0 or j < 0 or board[i][j] == 'X':
                return (NEG, 0)

            if i == 0 and j == 0:
                return (0, 1) # ek way mila yaha reach karne ka

            best = NEG
            ways = 0

            for dx, dy in dirs:
                score, cnt = f(i + dx, j + dy)

                if score > best:
                    best = score
                    ways = cnt

                elif score == best:
                    ways += cnt
                    ways %= MOD

            if best == NEG:
                return (NEG, 0)

            val = 0
            if board[i][j].isdigit():
                val = int(board[i][j])
            
            return (best + val, ways)

        mx_sum, ways = f(m - 1, m - 1)

        if mx_sum == NEG:
            return [0, 0]

        return [mx_sum, ways]