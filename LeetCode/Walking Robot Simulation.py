from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        n = len(commands)
        x = y = 0

        dir = "N"

        obstacles = set((ox, oy) for ox, oy in obstacles)
        mx_dist = 0

        for cmd in commands:
            if cmd == -2: # left jana hai
                if dir == "N":
                    dir = "W"

                elif dir == "W":
                    dir = "S"

                elif dir == "S":
                    dir = "E"

                else:
                    dir = "N"


            elif cmd == -1: # right jana hai
                if dir == "N":
                    dir = "E"

                elif dir == "E":
                    dir = "S"

                elif dir == "S":
                    dir = "W"

                else:
                    dir = "N"

            else:
                for _ in range(cmd):
                    nx, ny = x, y

                    if dir == "N": ny += 1
                    elif dir == "E": nx += 1
                    elif dir == "S": ny -= 1
                    else: nx -= 1

                    if (nx, ny) in obstacles:
                        break

                    x, y = nx, ny

                    mx_dist = max(mx_dist, x ** 2 + y ** 2)

        return mx_dist