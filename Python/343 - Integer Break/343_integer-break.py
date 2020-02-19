from leezy import Solution, solution


class Q343(Solution):
    @solution
    def integerBreak(self, n):
        # 36ms 82.92%
        dp = [0] * (n+1)
        # dp[i]: max product we can get when we split i into >= 2 parts
        dp[2] = 1
        for i in range(3, n+1):
            for j in range(1, i-1):
                # split into >= 3 parts: dp[i-j] * j
                # split into 2 parts: j * (i-j)
                dp[i] = max(dp[i], dp[i-j] * j, j * (i-j))
        return dp[n]

    @solution
    def integer_break(self, n):
        if n <= 3:
            return n - 1
        dp = [1] * (n+1)
        dp[1:5] = range(1, 5)
        # dp[i]: max product we can get when we split i into >= 1 parts
        # when i >= 5, only 1 part is absolutely not the max product,
        # it is safe to use dp[i]
        for i in range(5, n+1):
            dp[i] = max(dp[i-j] * j for j in range(1, i))
        return dp[n]

    @solution
    def integer_break_greedy(self, n):
        # greedy
        # 2 x (n-2) > n
        # 3 x (n-3) > n
        # 4 x (n-2) = 2 x 2 x (n-4)
        # 5 x (n-5) < 3 x 2 x (n-5)
        # 7 x (n-7) < 3 x 2 x 2 x (n-7): 7..n can be reduce to 3s or 2s again
        # dig more 3 from n, if 4 left, mutiple 4, if 2 left, multiple 2
        if n <= 3:
            return n - 1
        threes, r = divmod(n, 3)
        if r == 1:  # 4 left
            return (3 ** (threes-1)) * 4
        elif r == 2:  # 2 left
            return (3 ** threes) * 2
        else:  # all 3s
            return 3 ** threes

    @solution
    def integer_break_greedy_overflow(self, n):
        if n <= 3:
            return n - 1
        KMOD = 10**9 + 7
        ans = 1
        while n > 4:
            ans = (ans * 3) % KMOD
            n -= 3
        return (ans * n) % KMOD


def main():
    q = Q343()
    q.add_case(q.case(2).assert_equal(1))
    q.add_case(q.case(10).assert_equal(36))
    q.add_case(q.case(20).assert_equal(1458))
    q.run()


if __name__ == "__main__":
    main()
