from typing import Counter, List


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        n = len(nums)

        freq = Counter(nums)
        ans = 0
        
        if 1 in freq:
            ones = freq[1]
            ans = max(ans, ones if ones & 1 else ones - 1)

        for x in freq:
            if x == 1: continue

            cur = x
            cnt = 0

            while cur in freq:
                if freq[cur] >= 2:
                    cnt += 2
                    cur *= cur

                else:
                    cnt += 1
                    break

            ans = max(ans, cnt if cnt & 1 else cnt - 1)

        return ans