from collections import defaultdict, deque

class Solution:
    def minJumps(self, nums):
        n = len(nums)

        mp = defaultdict(list)
        maxEl = 0

        for i in range(n):
            mp[nums[i]].append(i)
            maxEl = max(maxEl, nums[i])

        isPrime = [True] * (maxEl + 1)
        isPrime[0] = False
        isPrime[1] = False

        num = 2
        while num * num <= maxEl:
            if isPrime[num]:
                multiple = num * num

                while multiple <= maxEl:
                    isPrime[multiple] = False
                    multiple += num

            num += 1

        q = deque([0])
        visited = [False] * n
        visited[0] = True

        seen = set()
        steps = 0

        while q:
            size = len(q)

            while size:
                i = q.popleft()

                if i == n - 1:
                    return steps

                if i - 1 >= 0 and not visited[i - 1]:
                    q.append(i - 1)
                    visited[i - 1] = True

                if i + 1 < n and not visited[i + 1]:
                    q.append(i + 1)
                    visited[i + 1] = True

                if not isPrime[nums[i]] or nums[i] in seen:
                    size -= 1
                    continue

                multiple = nums[i]
                while multiple <= maxEl:
                    if multiple in mp:
                        for j in mp[multiple]:
                            if not visited[j]:
                                q.append(j)
                                visited[j] = True

                    multiple += nums[i]

                seen.add(nums[i])
                size -= 1

            steps += 1

        return steps