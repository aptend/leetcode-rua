from random import uniform


class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.offset_x = x_center
        self.offset_y = y_center
        self.r = radius

    def randPoint(self):
        r = self.r
        x = y = r
        while x*x + y*y > r*r:
            x = uniform(-r, r)
            y = uniform(-r, r)
        return [x + self.offset_x, y + self.offset_y]


def main():
    rng = Solution(2, 0, 0)
    print([rng.randPoint() for _ in range(5)])


if __name__ == '__main__':
    main()
