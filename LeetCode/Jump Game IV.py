from typing import DefaultDict, Deque, List


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)

        if n == 1:
            return 0

        pos = DefaultDict(list)
        for i, x in enumerate(arr):
            pos[x].append(i)

        q = Deque() # steps, index
        q.append((0, 0))
        vis = {0}


        while q:
            steps, cur = q.popleft()

            if cur == n - 1:
                return steps


            if (cur - 1) >= 0 and (cur - 1) not in vis:
                q.append((steps + 1, cur - 1))
                vis.add(cur - 1)

            if (cur + 1) < n and (cur + 1) not in vis:
                q.append((steps + 1, cur + 1))
                vis.add(cur + 1)


            for nei in pos[arr[cur]]:
                if nei not in vis:
                    vis.add(nei)
                    q.append((steps + 1, nei))

            pos[arr[cur]].clear()
