class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        INF = float('inf')
        ans = 0

        last_lower = [-1] * 26
        first_upper = [INF] * 26

        for i, ch in enumerate(word):

            if ch.islower():
                idx = ord(ch) - ord('a')

                last_lower[idx] = i

            else:

                idx = ord(ch) - ord('A')

                if first_upper[idx] == INF:
                    first_upper[idx] = i

        for i in range(26):
            if last_lower[i] != -1 and first_upper[i] != INF:
                if last_lower[i] < first_upper[i]:
                    ans += 1

        return ans