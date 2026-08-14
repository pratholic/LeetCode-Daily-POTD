from collections import defaultdict

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)

        mx = 0

        for i in range(n):
            mp = defaultdict(int)

            for j in range(i, n):
                if mp[s[j]] < 2:
                    mp[s[j]] += 1

                else:
                    break

                mx = max(mx, j - i + 1)

        return mx                    