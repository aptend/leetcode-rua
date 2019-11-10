from leezy import Solution, solution


class Q072(Solution):
    @solution
    def minDistance(self, word1, word2):
        # 68ms 99.63%  weird
        m, n = len(word1), len(word2)
        memo = [[-1] * (n+1) for _ in range(m+1)]
        def sub_dis(i, j):
            if i == 0:
                return j
            if j == 0:
                return i
            if memo[i][j] >= 0:
                return memo[i][j]
            if word1[i-1] == word2[j-1]:
                memo[i][j] = sub_dis(i-1, j-1)
            else:
                memo[i][j] = 1 + min(sub_dis(i-1, j-1), # replace
                                     sub_dis(i-1, j), # remove
                                     sub_dis(i, j-1)) # insert
            return memo[i][j]
        return sub_dis(m, n)

    @solution
    def edit_dis(self, word1, word2):
        # 136ms 83%
        m, n = len(word1), len(word2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j-1],
                                       dp[i-1][j],
                                       dp[i][j-1])
        return dp[m][n]



def main():
    q = Q072()
    q.add_args('horse', 'ros')
    q.run()


if __name__ == "__main__":
    main()
