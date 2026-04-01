from typing import List


class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)

        robots = []
        for i in range(n):
            robots.append((positions[i], healths[i], directions[i], i))

        stack = []
        robots.sort(key = lambda x : x[0])

        for pos, health, direction, idx in robots:
            if direction == 'R':
                stack.append([health, direction, idx])

            else:
                cur_health = health

                while stack and stack[-1][1] == 'R':
                    top_health, _, top_idx = stack[-1]

                    if top_health < cur_health:
                        stack.pop()
                        cur_health -= 1
                    elif top_health > cur_health:
                        cur_health = 0
                        stack[-1][0] -= 1
                        break

                    else:
                        stack.pop()
                        cur_health = 0
                        break

                
                if cur_health > 0:
                    stack.append([cur_health, direction, idx])

        res = [0] * n
        for health, _, idx in stack:
            res[idx] = health

        return [x for x in res if x > 0]