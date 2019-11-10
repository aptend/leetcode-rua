from leezy import Solution, solution


class Q064(Solution):
    @solution
    def minPathSum(self, grid):
        # 84ms 51.73%
        if not grid:
            return 0
        # start point is (1, 1) and end point is (m, n)
        # dp[i][j] means min cost from left-top to (i,j)
        m, n = len(grid), len(grid[0])
        dp = [[float('inf')]*(n+1) for _ in range(m+1)]
        dp[0][1] = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i-1][j-1]
        return dp[m][n]

    @solution
    def min_path_sum(self, grid):
        # 80ms 74.10%
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [float('inf')] * (n+1)
        dp[1] = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[j] = min(dp[j], dp[j-1]) + grid[i-1][j-1]
        return dp[n]


def main():
    q = Q064()
    q.add_args([[1, 3, 1], [1, 5, 1], [4, 2, 1]])
    q.run()


if __name__ == "__main__":
    main()
