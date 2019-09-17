from leeyzer import Solution, solution


class Q1143(Solution):
    @solution
    def longestCommonSubsequence(self, text1, text2):
        # 384ms 79.93%
        m, n = len(text1), len(text2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]

    def longest(self, text1, text2):
        # 1204ms 9%
        memo = {}
        def cnt_common(i, j):
            if i == -1 or j == -1:
                return 0
            if (i, j) in memo:
                return memo[i, j]

            if text1[i] == text2[j]:
                res = cnt_common(i-1, j-1) + 1
            else:
                res = max(cnt_common(i-1, j), cnt_common(i, j-1))
            memo[i, j] = res
            return res
        m, n = len(text1), len(text2)
        return cnt_common(m-1, n-1)


def main():
    q = Q1143()
    q.add_args('abcde', 'ace')
    q.run()


if __name__ == "__main__":
    main()
