from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if arr[start] == 0:
            return True

        n = len(arr)
        vis = set()

        def f(idx):
            if idx >= n:
                return False

            if idx < 0:
                return False

            if arr[idx] == 0:
                return True

            if idx in vis: return False

            vis.add(idx)

            if f(idx + arr[idx]) or f(idx - arr[idx]):
                return True

            return False

        return f(start)