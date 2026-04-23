from typing import DefaultDict, List


class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)

        mp = DefaultDict(list)

        for i, x in enumerate(nums):
            mp[x].append(i)

        ans = [0] * n

        for pos in mp.values():
            k = len(pos)
            pref = [0] * k
            pref[0] = pos[0]

            for i in range(1, k):
                pref[i] += (pref[i - 1] + pos[i])

            for i in range(k):
                left = i * pos[i] - (pref[i - 1] if (i) > 0 else 0)
                right = (pref[k - 1] - pref[i]) - (k - i - 1) * pos[i]

                ans[pos[i]] = left + right

        return ans