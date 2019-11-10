from leezy import Solution, solution


class Q115(Solution):
    @solution
    def numDistinct(self, s, t):
        # 132ms 67.19%
        # like 712 583
        m, n = len(s), len(t)
        memo = [[-1]*(n+1) for _ in range(m+1)]
        def sub_num(i, j):
            if i < j:
                return 0
            if j == 0:
                return 1
            if memo[i][j] >= 0:
                return memo[i][j]
            ways = sub_num(i-1, j)
            if s[i-1] == t[j-1]:
                ways += sub_num(i-1, j-1)
            memo[i][j] = ways
            return ways
        return sub_num(m, n)

    @solution
    def num_distinct(self, s, t):
        # 132ms
        m, n = len(s), len(t)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = 1
        for i in range(1, m+1):
            for j in range(1, min(n+1, i+1)):
                dp[i][j] = dp[i-1][j]
                if s[i-1] == t[j-1]:
                    dp[i][j] += dp[i-1][j-1]
        return dp[m][n]



def main():
    q = Q115()
    q.add_args('aba', 'ba')
    q.add_args('rabbbit', 'rabbit')
    q.add_args('baggbag', 'bag')
    q.add_args('babgbag', 'bag')
    q.run()


"""
rabbbit rabbit

rabbbi rabbi -> 3
  rabbb rabb -> 3
    rabb rab -> 2
      rab ra -> 1
        ra ra -> 1
      rab rab -> 1
    rabb rabb -> 1
  rabbb rabbi -> 0
   rabb rabbi -> 0

rabbbi rabbit -> 0
  rabbb rabbit -> 0
"""

if __name__ == "__main__":
    main()
