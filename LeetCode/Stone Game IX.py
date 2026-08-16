class Solution:
    def stoneGameIX(self, stones):
        f = [0, 0, 0]

        for x in stones:
            f[x % 3] += 1

        if f[0] & 1:
            return abs(f[1] - f[2]) >= 3
        else:
            return min(f[1], f[2]) >= 1