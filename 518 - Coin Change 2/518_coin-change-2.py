from leeyzer import Solution, solution

"""
    1   2   5
0   1   1   1
1   1   1   1
2   1   2   2
3   1   2   2
4   1   3   3
5   1   3   4
"""
class Q518(Solution):
    @solution
    def change(self, amount, coins):
        dp = [1] + [0] * amount
        for n in coins:
            for i in range(1, amount+1):
                used = 0
                if n <= i:
                    used = dp[i-n]
                # not_used = dp[i]
                # dp[i] = used + not_used
                dp[i] += used
        return dp[amount]

    @solution
    def change_concise(self, amount, coins):
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
