class Solution:
    def maxProduct(self, n: int) -> int:
        digits = []

        while n > 0:
            ld = n % 10
            digits.append(ld)
            n //= 10

        digits.sort()

        last = digits[-1]
        sec_last = digits[-2]

        return last * sec_last