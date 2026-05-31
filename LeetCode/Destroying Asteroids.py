from typing import List


class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        n = len(asteroids)

        asteroids.sort()

        for x in asteroids:
            if x > mass:
                return False

            mass += x

        return True