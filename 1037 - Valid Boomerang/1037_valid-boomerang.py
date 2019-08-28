from leeyzer import Solution, solution


class Q1037(Solution):
    @solution
    def isBoomerang(self, points):
        # 16ms 78.21%
        x1, x2, x3 = points[0][0], points[1][0], points[2][0]
        y1, y2, y3 = points[0][1], points[1][1], points[2][1]
        if x1 == x2 == x3:
            return False
        return (y3-y2) * (x2-x1) != (y2-y1) * (x3-x2)


def main():
    q = Q1037()
    q.add_args([[1, 1], [1, 2], [1, 3]])
    q.add_args([[2, 1], [3, 1], [6, 1]])
    q.add_args([[1, 1], [2, 3], [3, 2]])
    q.add_args([[1, 1], [2, 2], [3, 3]])
    q.run()


if __name__ == "__main__":
    main()
