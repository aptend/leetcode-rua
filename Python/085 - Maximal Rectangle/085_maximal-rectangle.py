from leezy import Solution, solution


class Q085(Solution):
    @solution
    def maximalRectangle(self, matrix):
        # 380ms 16.43%
        if not matrix:
            return 0
        # dp[i][j] means max length of horizontal '1's array ending at (i, j)
        m, n = len(matrix), len(matrix[0])
        g_max = 0
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1] == '0':
                    continue
                dp[i][j] = dp[i][j-1] + 1
                w, h, k = dp[i][j], 0, 0
                while dp[i-k][j]:
                    h += 1
                    w = min(w, dp[i-k][j])
                    g_max = max(g_max, w * h)
                    k += 1
        return g_max

def main():
    q = Q085()
    q.add_args([[]])
    q.add_args([['0']])
    q.add_args([['1']])
    q.add_args([['1', '0', '1', '0', '0'],
                ['1', '0', '1', '1', '1'],
                ['1', '1', '1', '1', '1'],
                ['1', '0', '0', '1', '0']])
    q.run()


if __name__ == "__main__":
    main()
