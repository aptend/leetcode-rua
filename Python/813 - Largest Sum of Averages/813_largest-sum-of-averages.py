from leezy import Solution, solution


class Q813(Solution):
    @solution
    def largestSumOfAverages(self, A, K):
        # 404ms 51.58%  Python3
        # dp[i][j] means max scores when partitioning A[:j] into i groups
        # then try every action to group A[j]
        # dp[i][j] = max(dp[i-1][j-n] + sum(A[j-n:j]) / n for n in 1..j)
        N, MIN = len(A), float('-inf')
        dp = [[MIN]*(N+1) for _ in range(K+1)]
        dp[0][0] = 0
        for i in range(1, K+1):
            for j in range(1, N+1):
                m_score, _sum = MIN, 0
                for n in range(1, j+1):
                    _sum += A[j-n]
                    m_score = max(m_score, dp[i-1][j-n] + _sum/n)
                dp[i][j] = m_score
        return dp[K][N]

    @solution
    def largest_sum_avg(self, A, K):
        # 320ms 64.37% Python3
        N, MIN = len(A), float('-inf')
        p_sum = [0] * (N+1) # prefix_sum
        for i in range(1, N+1):
            p_sum[i] = p_sum[i-1] + A[i-1]
        dp = [[MIN]*(N+1) for _ in range(K+1)]
        dp[0][0] = 0
        for i in range(1, K+1):
            for j in range(1, N+1):
                dp[i][j] = max(dp[i-1][j-n] + (p_sum[j]-p_sum[j-n]) / n for n in range(1, j+1))
        return dp[K][N]


def main():
    q = Q813()
    q.add_args([9, 1], 1)
    q.add_args([9, 1, 2, 3, 9], 3)
    q.add_args([1, 2, 3, 4, 5, 6, 7], 4)
    q.run()


if __name__ == "__main__":
    main()
