from typing import List


class Robot:

    def __init__(self, width: int, height: int):
        self.grid = [[0] * width for _ in range(height)]
        self.x, self.y = 0, 0
        self.dir = "East"
        self.width = width
        self.height = height

        self.peri = 2 * (width + height) - 4

    def valid(self, i, j):
        return i >= 0 and i < self.width and j >= 0 and j < self.height

    def step(self, num: int) -> None:

        num %= self.peri
        if num == 0:
            num = self.peri
            
        for _ in range(num):
            while True:
                nx, ny = self.x, self.y

                if self.dir == "North": ny += 1
                elif self.dir == "South": ny -= 1
                elif self.dir == "East": nx += 1
                else: nx -= 1

                if self.valid(nx, ny):
                    self.x = nx
                    self.y = ny
                    break

                else:
                    if self.dir == "North": self.dir = "West"
                    elif self.dir == "South": self.dir = "East"
                    elif self.dir == "East": self.dir = "North"
                    else: self.dir = "South"


    def getPos(self) -> List[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        return self.dir


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()