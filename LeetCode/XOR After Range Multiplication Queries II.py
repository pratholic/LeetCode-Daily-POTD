from typing import DefaultDict, List
from math import ceil, sqrt

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = (10 ** 9) + 7

        def pow(a, b):
            if b == 0:
                return 1

            half = pow(a, b // 2)
            res = (half * half) % MOD

            if b & 1:
                res = (res * a) % MOD

            return res

        n = len(nums)
        block_size = ceil(sqrt(n))
        small_k_mp = DefaultDict(list)

        for l, r, k, v in queries:

            if k >= block_size:
                for i in range(l, r + 1, k):
                    nums[i] *= v
                    nums[i] %= MOD

            else:
                small_k_mp[k].append([l, r, v])

        for k, all_queries in small_k_mp.items():

            diff = [1] * n

            for l, r, v in all_queries:

                diff[l] *= v
                diff[l] %= MOD

                steps = (r - l) // k
                nxt = l + (steps + 1) * k

                if nxt < n:
                    diff[nxt] = (diff[nxt] * pow(v, MOD - 2)) % MOD

            
            for i in range(n):
                if (i - k) >= 0:
                    diff[i] *= diff[i - k]
                    diff[i] %= MOD

            for i in range(n):
                nums[i] *= diff[i]
                nums[i] %= MOD

        xr = 0
        for i in nums:
            xr ^= i

        return xr