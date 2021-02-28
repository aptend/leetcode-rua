from leezy import solution, Solution


class Q123(Solution):
    @solution
    def maxProfit(self, prices):
        dp1_hold = dp2_hold = float('-inf')
        dp1_free = dp2_free = 0
        for p in prices:
            dp2_free = max(dp2_free, dp2_hold + p)
            dp2_hold = max(dp2_hold, dp1_free - p)

            dp1_free = max(dp1_free, dp1_hold + p)
            dp1_hold = max(dp1_hold, 0 - p)

        return max(dp2_free, dp2_hold)


def main():
    q = Q123()
    q.add_case(q.case([3, 3, 5, 0, 0, 3, 1, 4]).assert_equal(6))
    q.add_case(q.case([1, 2, 3, 4, 5]).assert_equal(4))
    q.run()


if __name__ == '__main__':
    main()
