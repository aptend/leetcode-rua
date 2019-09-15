from leeyzer import Solution, solution


class Q063(Solution):
    @solution
    def uniquePathsWithObstacles(self, obstacleGrid):
        # 32ms 69.73%
        grid = obstacleGrid
        if not grid:
            return 0
        # start point is (1, 1) and end point is (m, n)
        # dp[i][j] means how many ways from left-top to (i,j)
        # dp[i][j] = 0 when running into an obstacle
        m, n = len(grid), len(grid[0])
        dp = [[0]*(n+1) for _ in range(m+1)]
        dp[0][1] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                if grid[i-1][j-1] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m][n]

    @solution
    def unique_paths_with_obstacles(self, obstacleGrid):
        # 24ms 97.54%
        # dimension reduction
        grid = obstacleGrid
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [0] * (n+1)
        dp[1] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                if grid[i-1][j-1] == 1:
                    dp[j] = 0
                else:
                    dp[j] += dp[j-1]
        return dp[n]


def main():
    q = Q063()
    q.add_args([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
    q.add_args([[0, 0, 1], [0, 1, 0], [0, 0, 0]])
    q.run()


if __name__ == "__main__":
    main()
