from typing import List


class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort(key = lambda x : x[0])

        positions = []
        for f in factory:
            positions.extend([f[0]] * f[1])

        dp = [[-1] * len(positions) for _ in range(len(robot))]
        def f(idx, cur_factory):
            if idx >= len(robot):
                return 0

            if cur_factory >= len(positions):
                return float('inf')

            if dp[idx][cur_factory] != -1:
                return dp[idx][cur_factory]

            take = abs(positions[cur_factory] - robot[idx]) + f(idx + 1, cur_factory + 1)
            skip = f(idx, cur_factory + 1)

            dp[idx][cur_factory] = min(take, skip)
            return dp[idx][cur_factory]

        return f(0, 0)