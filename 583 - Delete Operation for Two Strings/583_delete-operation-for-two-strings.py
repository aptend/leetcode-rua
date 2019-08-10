from leeyzer import Solution, solution


class Q583(Solution):
    @solution
    def minDistance(self, word1, word2):
        # 516ms 5%
        memo = {}
        def sub_min_dis(w1, w2):
            if w1 == w2:
                return 0
            if w1 == '' or w2 == '':
                return len(w1 or w2)
            if (w1, w2) in memo:
                return memo[(w1, w2)]
            if w1[-1] == w2[-1]:
                memo[(w1, w2)] = sub_min_dis(w1[:-1], w2[:-1])
            else:
                memo[(w1, w2)] = 1 + min(sub_min_dis(w1[:-1], w2),
                                         sub_min_dis(w1, w2[:-1]))
            return memo[(w1, w2)]
        return sub_min_dis(word1, word2)
    
    @solution
    def minDistance_idx(self, word1, word2):
        # 272ms 53.10%
        m, n = len(word1), len(word2)
        memo = [[-1] * (n+1) for _ in range(m+1)]
        def sub_min_dis(i, j):
            if i == 0:
                return j
            if j == 0:
                return i
            if memo[i][j] >= 0:
                return memo[i][j]
            if word1[i-1] == word2[j-1]:
                memo[i][j] = sub_min_dis(i-1, j-1)
            else:
                memo[i][j] = 1 + min(sub_min_dis(i-1, j),
                                     sub_min_dis(i, j-1))
            return memo[i][j]
        return sub_min_dis(m, n)
    
    @solution
    def min_dis_bottom_up(self, word1, word2):
        # 236ms 88.44%
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
                    dp[i][j] = 1 + min(dp[i-1][j],
                                       dp[i][j-1])
        return dp[m][n]





def main():
    q = Q583()
    q.add_args('sea', 'eat')
    q.add_args('aabcd', 'abcd')
    q.run()


if __name__ == "__main__":
    main()
