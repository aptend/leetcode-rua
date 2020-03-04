from leezy import solution, Solution
from collections import defaultdict

class Q956(Solution):
    @solution
    def tallestBillboard(self, rods):
        # 516 ms, 94.12%
        # this is incredible
        dp = defaultdict(int)
        dp[0] = 0
        for x in rods:
            for diff, a in list(dp.items()):
                d1 = diff + x
                dp[d1] = max(dp[d1], a)
                d2 = abs(diff-x)
                dp[d2] = max(dp[d2], a+min(diff, x))
        return dp[0]


def main():
    q = Q956()
    q.add_case(q.case([1, 2, 3, 6]).assert_equal(6))
    q.add_case(q.case([1, 2, 3, 4, 5, 6]).assert_equal(10))
    q.add_case(q.case([1, 2]).assert_equal(0))
    q.run()


if __name__ == '__main__':
    main()
