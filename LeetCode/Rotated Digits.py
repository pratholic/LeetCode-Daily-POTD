class Solution:
    def rotatedDigits(self, n: int) -> int:
        ans = 0

        for i in range(1, n + 1):
            s = str(i)
            if '2' in s or '5' in s or '6' in s or '9' in s:
                if '3' not in s and '4' not in s and '7' not in s:
                    ans += 1

        return ans