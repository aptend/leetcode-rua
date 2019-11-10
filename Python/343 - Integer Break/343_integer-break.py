from leezy import Solution, solution


class Q343(Solution):
    @solution
    def integerBreak(self, n):
        # 36ms 82.92%
        dp = [0] * (n+1)
        dp[2] = 1
        for i in range(3, n+1):
            for j in range(1, i-1):
                dp[i] = max(dp[i], dp[i-j] * j, j * (i-j))
        return dp[n]


def main():
    q = Q343()
    q.add_args(2)
    q.add_args(10)
    q.run()


if __name__ == "__main__":
    main()
