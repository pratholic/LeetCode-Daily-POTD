class Solution:
    def bitwiseComplement(self, n: int) -> int:
        n = bin(n)[2:]

        ans = ""
        for i in range(len(n)):
            if n[i] == '1':
                ans += '0'

            else:
                ans += '1'

        res = 0
        ans = ans[::-1]
        for i in range(len(ans) - 1, -1, -1):
            if ans[i] == '1':
                res += (1 << i)

        return res