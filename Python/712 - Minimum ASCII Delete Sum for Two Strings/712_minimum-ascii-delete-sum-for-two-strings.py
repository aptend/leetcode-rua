from leezy import Solution, solution


class Q712(Solution):
    @solution
    def minimumDeleteSum(self, s1, s2):
        # 668ms 55.52%  too many ord() calls
        m, n = len(s1), len(s2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            dp[i][0] = dp[i-1][0] + ord(s1[i-1])
        for j in range(1, n+1):
            dp[0][j] = dp[0][j-1] + ord(s2[j-1])
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j] + ord(s1[i-1]),
                                   dp[i][j-1] + ord(s2[j-1]))
        return dp[m][n]


def main():
    q = Q712()
    q.add_args('sea', 'eat')
    q.add_args('delete', 'leet')
    q.run()


if __name__ == "__main__":
    main()
