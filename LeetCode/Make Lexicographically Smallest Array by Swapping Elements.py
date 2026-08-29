from typing import List


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)

        pairs = sorted([(val, idx) for idx, val in enumerate(nums)])

        ans = [0] * n

        s = 0

        while s < n:
            e = s

            while e + 1 < n and pairs[e + 1][0] - pairs[e][0] <= limit:
                e += 1

            vals = [pairs[i][0] for i in range(s, e + 1)]

            indices = [pairs[i][1] for i in range(s, e + 1)]

            indices.sort()

            for v, i in zip(vals, indices):
                ans[i] = v

            s = e + 1

        return ans