from leezy import solution, Solution


class Q1278(Solution):
    @solution
    def palindromePartition(self, s, k):
        # 248mw 62,05%
        N = len(s)
        change = [[0] * N for _ in range(N)]
        for l in range(2, N+1):
            for i in range(N-l+1):
                j = i + l - 1
                change[i][j] = int(s[i] != s[j]) + change[i+1][j-1]

        # dp[i][k] min change for s[..=i] into k group
        dp = [[float('inf')] * (k+1) for _ in range(N)]
        K = k
        for k in range(1, K+1):
            for j in range(k-1, N):
                if k == 1:
                    dp[j][k] = change[0][j]
                else:
                    for i in range(1, j+1):
                        dp[j][k] = min(dp[j][k], dp[i-1][k-1]+change[i][j])
        return dp[N-1][K]


def main():
    q = Q1278()
    q.add_case(q.case('abc', 2).assert_equal(1))
    q.add_case(q.case('aabbc', 3).assert_equal(0))
    q.add_case(q.case('leetcode', 8).assert_equal(0))
    q.run()

if __name__ == '__main__':
    main()
