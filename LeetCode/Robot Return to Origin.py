class Solution:
    def judgeCircle(self, moves: str) -> bool:
        n = len(moves)

        left, right, up, down = 0, 0, 0, 0

        for ch in moves:
            if ch == 'U': up += 1
            elif ch == 'D': down += 1
            elif ch == 'L': left += 1
            else: right += 1

        return left == right and up == down