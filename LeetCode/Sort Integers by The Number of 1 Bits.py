from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        n = len(arr)
        a = []
        for i, v in enumerate(arr):
            bits = bin(v)[2:]
            cnt = bits.count('1')
            a.append((v, cnt))

        lst = sorted(a, key = lambda x : (x[1], x[0]))

        return [x for x, y in lst]