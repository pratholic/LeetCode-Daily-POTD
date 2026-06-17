class Solution:
    def processStr(self, s: str, k: int) -> str:
        n = len(s)
        length = 0

        for ch in s:
            if ch.islower():
                length += 1

            elif ch == '#':
                length *= 2

            elif ch == '*' and length > 0:
                length -= 1

        if k >= length:
            return '.'

        for i in range(n - 1, -1, -1):
            ch = s[i]

            if ch.islower():
                if k == length - 1:
                    return ch

                length -= 1

            elif ch == '#':
                length //= 2

                if k >= length:
                    k = k - length

            elif ch == '*':
                length += 1

            elif ch == '%':
                k = length - 1 - k

        return '.'