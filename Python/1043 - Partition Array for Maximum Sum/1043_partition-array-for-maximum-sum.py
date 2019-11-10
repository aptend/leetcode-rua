from leezy import Solution, solution


class Q1043(Solution):
    @solution
    def maxSumAfterPartitioning(self, A, K):
        # 388ms 78.42%
        N, MIN = len(A), float('-inf')
        # dp[i] means max sum after patitioning A[:i]
        dp = [0] * (N+1)
        for i in range(1, N+1):
            rolling_m = MIN
            # the last n numbers form a group
            for n in range(1, min(i+1, K+1)):
                rolling_m = max(rolling_m, A[i-n])
                dp[i] = max(dp[i], dp[i-n]+rolling_m*n)
        return dp[N]


def main():
    q = Q1043()
    q.add_args([1, 15, 7, 9, 2, 5, 10], 3)
    q.run()


if __name__ == "__main__":
    main()
