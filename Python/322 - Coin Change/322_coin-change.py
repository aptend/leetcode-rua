from leezy import Solution, solution


class Q322(Solution):

    @solution
    def change_2D(self, coins, amount):
        # 1696ms 14.85%
        # this shares the similar pattern with 518. unbounded knapsack problem
        # dp[i][j] means minimum coins to sum up to amount j using coins[i:]
        # dp[i][j] = min(dp[i-1][j], dp[i][j-coin]+1)
        N, MAX = len(coins), amount + 1
        dp = [[MAX] * (amount+1) for _ in range(N+1)]
        for i in range(N+1):
            dp[i][0] = 0
        for i in range(1, N+1):
            coin = coins[i-1]
            for j in range(1, amount+1):
                dp[i][j] = dp[i-1][j]  # do not use current coin
                if j >= coin:
                    # use current coin
                    dp[i][j] = min(dp[i][j], dp[i][j-coin]+1)
        return dp[N][amount] if dp[N][amount] != MAX else -1

    @solution
    def change_1D(self, coins, amount):
        # 960ms 81.72%
        MAX = amount + 1
        dp = [MAX] * (amount+1)
        dp[0] = 0
        for coin in coins:
            for j in range(coin, amount+1):
                dp[j] = min(dp[j], dp[j-coin]+1)
        return dp[amount] if dp[amount] != MAX else -1

    @solution
    def coinChange(self, coins, amount):
        # 1068ms
        if amount < 0:
            return -1
        coins = sorted(coins)
        dp = [0] + [float('inf')] * amount
        for i in range(1, amount+1):
            for c in coins:
                if c > i:
                    break
                dp[i] = min(dp[i], dp[i-c]+1)
        return dp[amount] if dp[amount] != float('inf') else -1

    @solution
    def coin_change(self, coins, amount):
        # 1996ms
        memo = {}
        coins = sorted(coins)
        r = self.dfs(coins, amount, memo)
        return r if r != float('inf') else -1

    def dfs(self, coins, amount, memo):
        if amount == 0:
            return 0
        if amount in memo:
            return memo[amount]

        r = float('inf')
        for c in coins:
            if c > amount:
                break
            r = min(r, self.dfs(coins, amount - c, memo)+1)
        memo[amount] = r
        return r

    @solution
    def coin_change_prune(self, coins, amount):
        least = [float('inf')]
        coins = sorted(coins, reverse=True)
        self.dfs_prune_boilerplate(coins, 0, amount, 0, least)
        return least[0] if least[0] != float('inf') else -1

    def dfs_prune(self, coins, s, amount, count, least):
        # 144ms 99.23%
        c = coins[s]
        if s == len(coins) - 1:  # quit earlier
            if amount % c == 0:
                least[0] = min(least[0], count + amount // c)
        else:
            for k in range(amount // c, -1, -1):
                if count + k >= least[0]:  # !! important
                    break
                self.dfs_prune(coins, s+1, amount - k*c, count+k, least)

    def dfs_prune_boilerplate(self, coins, s, amount, count, least):
        # 192ms
        if s >= len(coins):
            if amount == 0:
                least[0] = min(least[0], count)
            return
        c = coins[s]
        for k in range(amount // c, -1, -1):
            if count + k >= least[0]:
                break
            self.dfs_prune_boilerplate(
                coins, s+1, amount - k*c, count+k, least)


def main():
    q = Q322()
    q.add_args([1, 2, 5], 11)
    q.add_args([1, 2, 5], 0)
    q.add_args([1, 2, 5], 53)
    q.add_args([2, 5], 1)
    q.run()


if __name__ == "__main__":
    main()
