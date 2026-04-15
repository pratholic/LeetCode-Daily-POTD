from typing import List


class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)

        exist = False
        for s in words:
            if s == target:
                exist = True
                break

        if not exist:
            return -1

        ans = float('inf')
        prev_dist = 0

        i = startIndex
        while words[i] != target:
            prev_dist += 1
            i = (i - 1 + n) % n

        ans = min(ans, prev_dist)

        j = startIndex
        nxt_dist = 0
        while words[j] != target:
            nxt_dist += 1

            j = (j + 1) % n

        ans = min(ans, nxt_dist)

        return ans