class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        res = 0
        for num in range(1, n + 1):
            bits = len(bin(num)[2:])

            res = (res << bits) + num
            res %= MOD

        return res