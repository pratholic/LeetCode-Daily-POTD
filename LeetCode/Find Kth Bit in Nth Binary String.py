class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = [""] * (n)
        s[0] = "0"

        for i in range(1, n):
            prev = s[i - 1]

            invert = ""
            for ch in prev:
                if ch == '0':
                    invert += '1'

                else:
                    invert += '0'

            invert = invert[::-1]

            s[i] = prev + "1" + invert

        return s[n - 1][k - 1]