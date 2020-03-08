from leezy import solution, Solution


class Q1359(Solution):
    @solution
    def countOrders(self, n):
        # 1924 ms, 5.11%
        # dp[i, j] means how many ways to get i items picked and j items delivered
        # start: dp[0, 0] = 1
        # goal: dp[n, n]
        # [0, 0] = 1
        # [1, 0] = 3  [1, 1] = 3
        # [2, 0] = 6  [2, 1] = 6*2+3*2 = 18  [2, 2] = 18
        # [3, 0] = 6  [3, 1] = 18+6*3 = 36  [3, 2] = 18 + 36 * 2 = 90 [3, 3] = 90
        dp = [[0] * (n+1) for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(n+1):
            for j in range(i+1):
                if i < n:  # push to next row
                    dp[i+1][j] += dp[i][j] * (n-i)
                if j < i:  # push to right column
                    dp[i][j+1] += dp[i][j] * (i-j)
        return dp[n][n] % (10**9 + 7)


    @solution
    def count_orders(self, n):
        # 40 ms 13.40%
        # _ X _ X _
        # 3 + 2 + 1 = 6  -> f(2) = 6 * f(1) = 6
        # _ X _ X _ X _ X _
        # 5 + 4 + ... + 1 = 15 -> f(3) = 15 * f(2) = 90
        # 7 + 6 + ... + 1 = 28 -> f(4) = 28 * f(3) = 2520
        ans = 1
        kmod = 10**9 + 7
        for i in range(1, n+1):
            s = (i * (2*i - 1)) % kmod
            ans = (s * ans) % kmod
        return ans




def main():
    q = Q1359()
    q.add_case(q.case(0).assert_equal(1))
    q.add_case(q.case(1).assert_equal(1))
    q.add_case(q.case(2).assert_equal(6))
    q.add_case(q.case(3).assert_equal(90))
    q.add_case(q.case(4).assert_equal(2520))
    q.run()


if __name__ == '__main__':
    main()
