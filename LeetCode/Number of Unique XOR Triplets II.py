from typing import List


class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()

        pairs = set()
        triplets = set()

        for i, x in enumerate(nums):
            for val in nums[i : ]:
                pairs.add(val ^ x)

        for xy in pairs:
            for x in nums:
                triplets.add(xy ^ x)

        return len(triplets)