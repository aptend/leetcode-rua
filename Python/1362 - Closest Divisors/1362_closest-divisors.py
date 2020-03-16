from leezy import solution, Solution


class Q1362(Solution):
    @solution
    def closestDivisors(self, num):
        for x in range(int((num + 2) ** 0.5), 0, -1):
            diff = num + 1 - x * x
            d, r = divmod(diff, x)
            if r == 0:
                return [x, x+d]
            elif r == x-1:
                return [x, x+d+1]


def main():
    q = Q1362()
    q.add_case(q.case(8).assert_equal([3, 3]))
    q.add_case(q.case(1).assert_equal([1, 2]))
    q.add_case(q.case(2).assert_equal([2, 2]))
    q.add_case(q.case(3).assert_equal([2, 2]))
    q.add_case(q.case(123).assert_equal([5, 25]))
    q.run()


if __name__ == '__main__':
    main()
