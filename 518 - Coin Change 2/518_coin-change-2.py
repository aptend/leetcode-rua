from leeyzer import Solution, solution

"""
    1   2   5
0   1   1   1
1   1   1   1
2   1   2   2
3   1   2   2
4   1   3   3
5   1   3   4

 initial
   |
   v
   0   1   2
0  1   1   1  <- initial
1  0
2  0
3  0
4  0

ROUND1:
   0   1   2
0  1   1   1
       v
1  0 > 1
       v
2  0 > 1
       v
3  0 > 1
       v
4  0 > 1

ROUND2:
   0   1   2
0  1   1   1
1  0   1 > 1
2  0   1 > 2 < (0, 2)
3  0   1 > 2 < (1, 2)
4  0   1 > 3 < (2, 2)

"""


class Q518(Solution):
    @solution
    def change(self, amount, coins):
        # 372ms 26.98%
        # dp[i][j] means how many ways to sum up to amount j using coins[:i]
        N = len(coins)
        dp = [[0] * (amount+1) for _ in range(N+1)]
        # dp[i][0] means we always can change amount 0
        for i in range(N+1):
            dp[i][0] = 1
        for i in range(1, N+1):
            coin = coins[i-1]
            for j in range(1, amount+1):
                dp[i][j] = dp[i-1][j]  # do not use current coin
                if j >= coin:
                    dp[i][j] += dp[i][j-coin]  # use current coin
        return dp[N][amount]

    @solution
    def change_concise(self, amount, coins):
        # 100ms 92.18%
        dp = [1] + [0] * amount
        for n in coins:
            for i in range(n, amount+1):
                dp[i] += dp[i-n]
        return dp[amount]


def main():
    q = Q518()
    q.add_args(5, [1, 2, 5])
    q.add_args(777, [1, 2, 5, 10, 20, 50, 100])
    q.add_args(5, [3])
    q.run()


if __name__ == "__main__":
    main()
