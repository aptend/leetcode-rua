from leezy import solution, Solution


class Q1030(Solution):
    @solution
    def allCellsDistOrder(self, R, C, r0, c0):
        # 164ms 90.63%
        points = [[r, c] for r in range(R) for c in range(C)]
        return sorted(points, key=lambda p: abs(p[0]-r0) + abs(p[1]-c0))


def main():
    q = Q1030()
    q.add_case(q.case(1, 2, 0, 0))
    q.run()

if __name__ == '__main__':
    main()
