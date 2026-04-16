from bisect import *
from collections import defaultdict
from typing import List

from sortedcontainers import SortedList

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        mpp = defaultdict(SortedList)

        for i, x in enumerate(nums):
            mpp[x].add(i)

        ans = []

        for q in queries:
            arr = mpp[nums[q]]

            if len(arr) == 1:
                ans.append(-1)
                continue

            idx = bisect_left(arr, q)
            res = float('inf')

            if idx + 1 < len(arr):
                res = min(res, arr[idx + 1] - q)

            if idx - 1 >= 0:
                res = min(res, q - arr[idx - 1])

            res = min(res, n - (arr[-1] - q))
            res = min(res, n - (q - arr[0]))

            ans.append(res)

        return ans