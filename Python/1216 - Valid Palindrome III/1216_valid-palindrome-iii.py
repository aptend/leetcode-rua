from leezy import Solution, solution


class Q1216(Solution):
    @solution
    def isValidPalindrome(self, s, k):
        # we just need to find longest palindrome subsequence8
        # refer to 1143 longest common subsequence
        r = s[::-1]
        N = len(s)
        dp = [[0] * (N+1) for _ in range(N+1)]
        for i in range(1, N+1):
            for j in range(1, N+1):
                if s[i-1] == r[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[N][N] >= N - k



def main():
    q = Q1216()
    q.add_args('abcdeca', 2)
    q.run()


if __name__ == "__main__":
    main()
