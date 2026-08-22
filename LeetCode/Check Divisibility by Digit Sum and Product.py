class Solution:
    def checkDivisibility(self, n: int) -> bool:
        tmp = n
        sm = 0

        while tmp > 0:
            ld = tmp % 10
            sm += ld
            tmp //= 10

        tmp = n
        prod = 1
        while tmp > 0:
            ld = tmp % 10
            prod *= ld
            tmp //= 10

        return n % (sm + prod) == 0