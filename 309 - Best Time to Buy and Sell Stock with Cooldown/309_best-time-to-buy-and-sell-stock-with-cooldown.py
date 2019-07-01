from leeyzer import Solution, solution


class Q309(Solution):
    @solution
    def maxProfit(self, prices):
        # dp[i] max profit until i^{th} day when last transcation is:
        # 0: buying
        # 1: selling
        N = len(prices)
        dp = [[0, 0] for _ in range(N)]
        dp.append([float('-inf'), 0])
        for i, p in enumerate(prices):
            dp[i][0] = max(dp[i-1][0], dp[i-2][1] - p)
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + p)
        return max(dp[N-1][0], dp[N-1][1], 0)



def main():
    q = Q309()
    q.add_args([1, 2, 3, 0, 2])
    q.add_args([1, 2, 3, 4, 5])
    q.add_args([7, 5, 3, 2, 3])
    q.run()


if __name__ == "__main__":
    main()
