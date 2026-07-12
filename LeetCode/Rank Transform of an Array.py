from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ans = arr.copy()

        arr.sort()

        ranks = {}

        for x in arr:
            if x not in ranks:
                ranks[x] = len(ranks) + 1

        for i in range(len(ans)):
            ans[i] = ranks.get(ans[i])

        return ans