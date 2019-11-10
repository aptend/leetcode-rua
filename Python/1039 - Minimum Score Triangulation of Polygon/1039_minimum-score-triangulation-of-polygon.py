from leezy import Solution, solution


class Q1039(Solution):
    @solution
    def minScoreTriangulation(self, A):
        # 148ms 53.33%
        N = len(A)
        memo = [[None] * N for _ in range(N)]
        # memo[i][j] means min score when using A[i:j+1]
        def tri(i, j):
            if j - i <= 1:
                return 0
            if memo[i][j] is not None:
                return memo[i][j]
            min_s = float('inf')
            # based on edge `i->j`, try every possible vertex to form a triangle
            # i and j is min, max index, which makes us avoid mass trouble
            for k in range(i+1, j):
                min_s = min(min_s, tri(i, k) + tri(k, j) + A[i]*A[j]*A[k])
            memo[i][j] = min_s
            return min_s
        return tri(0, N-1)

    @solution
    def min_score_triangulation(self, A):
        # 76ms 83.39%
        N = len(A)
        dp = [[float('inf')] * N for _ in range(N)]
        # dp[i][j] means min score when using A[i:j+1]
        for l in range(2):
            for i in range(N-l):
                dp[i][i+l] = 0
        
        for l in range(2, N+1):
            for i in range(N-l):
                j = i + l
                for k in range(i+1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + A[i]*A[j]*A[k])
        return dp[0][N-1]


def main():
    q = Q1039()
    q.add_args([1, 2, 3])
    q.add_args([3, 7, 4, 5])
    q.add_args([1, 3, 1, 4, 1, 5])
    q.run()


if __name__ == "__main__":
    main()
