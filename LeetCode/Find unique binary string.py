from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        m = len(nums[0])
        st = set(nums)

        for mask in range(1 << m):
            cur = ""

            for i in range(m):
                if (mask >> i) & 1:
                    cur += '1'

                else:
                    cur += '0'

            if cur not in st:
                return cur

            
        return