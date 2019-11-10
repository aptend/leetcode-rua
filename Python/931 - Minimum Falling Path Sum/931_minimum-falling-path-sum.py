from leezy import Solution, solution


class Q931(Solution):
    @solution
    def minFallingPathSum(self, A):
        # 96ms 76.22%
        # grid version of 120. triangle
        if not A:
            return 0
        N, MAX = len(A), float('inf')
        dp = [[0] * (N+2) for _ in range(N+1)]
        for i in range(1, N+1):
            dp[i][0] = dp[i][-1] = MAX
            for j in range(1, N+1):
                dp[i][j] = A[i-1][j-1] + min(dp[i-1][j-1],
                                             dp[i-1][j],
                                             dp[i-1][j+1])
        return min(dp[N])

    @solution
    def min_falling_path_sum(self, A):
        # 84ms 99.26ms
        # using rolling array
        if not A:
            return 0
        N, MAX = len(A), float('inf')
        dp = [MAX] + A[0] + [MAX]
        cur_dp = [0] * (N+2)
        cur_dp[0] = cur_dp[-1] = MAX
        for i in range(1, N):
            for j in range(1, N+1):
                cur_dp[j] = A[i][j-1] + min(dp[j-1], dp[j], dp[j+1])
            cur_dp, dp = dp, cur_dp
        return min(dp)


def main():
    q = Q931()
    q.add_args([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    q.run()


if __name__ == "__main__":
    main()
