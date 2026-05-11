from typing import List


class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []

        def get(n):
            res = []
            while n:
                ld = n % 10
                res.append(ld)
                n //= 10

            return res[::-1]

        for i in range(n):
            numbers = get(nums[i])

            for x in numbers:
                ans.append(x)

        return ans