from leezy import Solution, solution


class Q062(Solution):
    @solution
    def uniquePaths(self, m, n):
        # 12ms 94.62%
        # dim reduction
        dp = [0] * (n+1)
        dp[1] = 1
        for _ in range(m):
            for i in range(1, n+1):
                dp[i] += dp[i-1]
        return dp[n]

    @solution
    def unique_paths(self, m, n):
        # 16ms 79.08%
        # start point is (1, 1) and end point is (m, n)
        # dp[i][j] means how many ways from left-top to (i,j)
        dp = [[0]*(n+1) for _ in range(m+1)]
        dp[0][1] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m][n]


def main():
    q = Q062()
    q.add_args(3, 2)
    q.add_args(7, 3)
    q.run()


if __name__ == "__main__":
    main()
