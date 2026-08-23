class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        left_q, right_q = 0, 0
        lsum, rsum = 0, 0

        half = n // 2

        for i in range(half):
            if num[i] == '?':
                left_q += 1

            else: lsum += int(num[i])

        for i in range(half, n):
            if num[i] == '?':
                right_q += 1

            else: rsum += int(num[i])

        total_q = left_q + right_q
        if total_q & 1:
            return True

        diff = lsum - rsum

        return (2 * diff) != 9 * (right_q - left_q)