from leeyzer import Solution, solution


class Q221(Solution):
    @solution
    def maximalSquare(self, matrix):
        # 160ms 89.57%
        if not matrix:
            return 0
        # dp[i][j] means max side length of the square whose right-bottom is (i,j)
        m, n = len(matrix), len(matrix[0])
        dp = [[0]*(n+1) for _ in range(m+1)]
        g_max = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1] == '0':
                    continue
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                g_max = max(dp[i][j], g_max)
        return g_max * g_max

    @solution
    def maximal_square(self, matrix):
        # 160ms
        if not matrix:
            return 0
        # rolling array for dim reduction
        m, n = len(matrix), len(matrix[0])
        dp = [0] * (n+1)
        cur_dp = [0] * (n+1)
        g_max = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1] == '0':
                    cur_dp[j] = 0 # important
                    continue
                cur_dp[j] = min(cur_dp[j-1], dp[j-1], dp[j]) + 1
                g_max = max(cur_dp[j], g_max)
            cur_dp, dp = dp, cur_dp
        return g_max * g_max


def main():
    q = Q221()
    q.add_args([['0']])
    q.add_args([['1','1'], ['1', '1']])
    q.add_args([['1', '0', '1', '0', '0'],
                ['1', '0', '1', '1', '1'],
                ['1', '1', '1', '1', '1'],
                ['1', '0', '0', '1', '0']])
    q.run()


if __name__ == "__main__":
    main()
