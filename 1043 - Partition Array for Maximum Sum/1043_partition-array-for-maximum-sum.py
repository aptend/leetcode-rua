from leeyzer import Solution, solution


class Q1043(Solution):
    @solution
    def maxSumAfterPartitioning(self, A, K):
        N = len(A)
        dp = [0] * (N+1)
        for i in range(N):
            rolling_m = float('-inf')
            for j in range(min(i+1, K)):
                rolling_m = max(rolling_m, A[i-j])
                dp[i] = max(dp[i], dp[i-j-1] + (j+1) * rolling_m)
        return dp[N-1]

def main():
    q = Q1043()
    q.add_args([1, 15, 7, 9, 2, 5, 10], 3)
    q.run()


if __name__ == "__main__":
    main()
