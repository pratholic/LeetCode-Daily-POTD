class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        p1 = 0
        p2 = 0

        for i in range(n):
            if i % 2 == 0:
                if s[i] != '0':
                    p1 += 1

                if s[i] != '1':
                    p2 += 1

            else:
                if s[i] != '1':
                    p1 += 1

                if s[i] != '0':
                    p2 += 1

        return min(p1, p2)