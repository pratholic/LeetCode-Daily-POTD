from typing import Counter, List


class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        f = Counter()
        n = len(nums)

        for i in range(n - k + 1):
            window = set(nums[i:i + k])
            
            for x in window:
                f[x] += 1
                
        mx = -1
        for key, v in f.items():
            if v == 1:
                mx = max(mx, key)

        return mx