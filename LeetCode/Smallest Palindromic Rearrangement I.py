class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)

        if n == 1:
            return s

        ans = [''] * n

        freq = [0] * 26
        for i, ch in enumerate(s):
            freq[ord(ch) - ord('a')] += 1

        idx = 0

        for i in range(26):
            ch = chr(i + ord('a'))

            while freq[i] >= 2:
                ans[idx] = ch
                ans[n - idx - 1] = ch

                freq[i] -= 2
                idx += 1

            if freq[i] == 1:
                ans[n // 2] = ch

        return "".join(ans)