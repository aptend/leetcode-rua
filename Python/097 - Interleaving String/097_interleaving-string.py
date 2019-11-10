from leezy import Solution, solution


class Q097(Solution):
    @solution
    def isInterleave(self, s1, s2, s3):
        # 16ms 95.04%
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        memo = [[None] * (n+1) for _ in range(m+1)]

        def is_intv(i, j):
            if memo[i][j] is not None:
                return memo[i][j]
            s3_idx = i + j
            if i == 0:
                ans = s3[:s3_idx] == s2[:j]
            elif j == 0:
                ans = s3[:s3_idx] == s1[:i]
            else:
                ans = ((s1[i-1] == s3[s3_idx-1] and is_intv(i-1, j)) or
                       (s2[j-1] == s3[s3_idx-1] and is_intv(i, j-1)))
            memo[i][j] = ans
            return ans
        return is_intv(m, n)

    @solution
    def is_interleave(self, s1, s2, s3):
        # 32ms
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        dp = [[False] * (n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = s1[:i] == s3[:i]
        for j in range(n+1):
            dp[0][j] = s2[:j] == s3[:j]
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = ((s1[i-1] == s3[i+j-1] and dp[i-1][j]) or
                            (s2[j-1] == s3[i+j-1] and dp[i][j-1]))
        return dp[m][n]


def main():
    q = Q097()
    q.add_args('', '', '')
    q.add_args('a', '', 'c')
    q.add_args('a', '', 'a')
    q.add_args('aabcc', 'dbbca', 'aadbbcbcac')
    q.add_args(s1="aabcc", s2="dbbca", s3="aadbbbaccc")
    q.run()


if __name__ == "__main__":
    main()
