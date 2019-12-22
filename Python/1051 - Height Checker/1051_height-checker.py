from leezy import solution, Solution


class Q1051(Solution):
    @solution
    def heightChecker(self, heights):
        return sum((a != b for a, b in zip(heights, sorted(heights))), 0)


def main():
    q = Q1051()
    q.add_case(q.case([1, 1, 4, 2, 1, 3]).assert_equal(3))
    q.run()

if __name__ == '__main__':
    main()
