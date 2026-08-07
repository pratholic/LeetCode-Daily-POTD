from math import gcd

class Solution:
    def free(self, req, ln):
        s = []

        for d in range(9, 1, -1):
            while req % d == 0:
                s.append(str(d))
                req //= d

        while len(s) < ln:
            s.append('1')

        s.reverse()
        return ''.join(s)

    def smallestNumber(self, num: str, t: int) -> str:
        n = len(num)

        x = t
        for p in (2, 3, 5, 7):
            while x % p == 0:
                x //= p

        if x != 1:
            return "-1"

        rf = [t] * (n + 1)

        for i in range(n):
            d = int(num[i])

            if d == 0:
                break

            rf[i + 1] = rf[i] // gcd(rf[i], d)

        if rf[n] == 1:
            return num

        z = num.find('0')
        zi = z if z != -1 else n - 1

        for i in range(zi, -1, -1):
            req = rf[i]
            fs = n - 1 - i

            for d in range(int(num[i]) + 1, 10):
                nr = req // gcd(req, d)
                s = self.free(nr, fs)

                if len(s) == fs:
                    return num[:i] + str(d) + s

        return self.free(t, n + 1)