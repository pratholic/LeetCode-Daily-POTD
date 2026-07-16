from math import gcd


class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)

        prefgcd = [float('inf')] * n
        mx = float('-inf')

        for i in range(n):
            mx = max(mx, nums[i])
            prefgcd[i] = gcd(nums[i], mx)

        prefgcd.sort()

        ans = 0
        i = 0
        j = n - 1

        while i < j:
            ans += gcd(prefgcd[i], prefgcd[j])

            i += 1
            j -= 1

        return ans