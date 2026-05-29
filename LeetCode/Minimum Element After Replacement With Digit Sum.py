from typing import List


class Solution:
    def minElement(self, nums: List[int]) -> int:

        def get(num):
            ans = 0
            while num > 0:
                ld = num % 10
                ans += ld
                num //= 10

            return ans
        
        digit_sums = []

        for x in nums:
            digit_sums.append(get(x))

        return min(digit_sums)