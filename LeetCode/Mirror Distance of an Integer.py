class Solution:
    def mirrorDistance(self, n: int) -> int:
        new_n = str(n)[::-1]
        new_n = int(new_n)

        return abs(n - new_n)