from leezy import solution, Solution


class Q836(Solution):
    @solution
    def isRectangleOverlap(self, rec1, rec2):
        ax1, ay1, ax2, ay2 = rec1
        bx1, by1, bx2, by2 = rec2
        assert ax1 <= ax2 and ay1 <= ay2
        assert bx1 <= bx2 and by1 <= by2
        return max(ax1, bx1) < min(ax2, bx2) and max(ay1, by1) < min(ay2, by2)


def main():
    q = Q836()
    q.add_case(q.case([0, 0, 2, 2], [1, 1, 3, 3]).assert_eqaul(True))
    q.add_case(q.case([0, 0, 1, 1], [1, 0, 2, 1]).assert_eqaul(False))
    q.run()


if __name__ == '__main__':
    main()
