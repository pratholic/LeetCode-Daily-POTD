class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        
        num = n

        while True:

            prod = 1
            tmp = num

            while tmp > 0:
                ld = tmp % 10
                prod *= ld
                tmp //= 10

            if prod % t == 0:
                return num

            num += 1

        return -1