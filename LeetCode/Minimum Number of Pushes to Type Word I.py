class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)

        times = [0] * 10
        idx = 2
        ans = 0

        for i, ch in enumerate(word):
            ans += times[idx] + 1
            times[idx] += 1

            if idx == 9:
                idx = 2

            else:
                idx += 1

        return ans