class Solution:
    def processStr(self, s: str) -> str:
        n = len(s)

        res = []

        for ch in s:
            if 'a' <= ch <= 'z':
                res.append(ch)

            elif ch == '*':
                if res:
                    res.pop()

            elif ch == '#':
                res = res + res

            elif ch == '%':
                res = res[::-1]

        return "".join(res)