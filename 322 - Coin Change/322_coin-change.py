from leeyzer import Solution, solution


class Q322(Solution):
    @solution
    def coinChange(self, coins, amount):
        coins = sorted(coins)
        dp = [0] + [float('inf')] * amount
        for i in range(1, amount+1):
            for c in coins:
                if c > i:
                    break
                dp[i] = min(dp[i], dp[i-c]+1)
        if amount < 0:
            return -1
        return dp[amount] if dp[amount] != float('inf') else -1

    @solution
    def coin_change(self, coins, amount):
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
        c = coins[s]
        if s == len(coins) - 1:
            if amount % c == 0:
                least[0] = min(least[0], count + amount // c)
        else:
            for k in range(amount // c, -1, -1):
                if count + k >= least[0]:  # !!
                    break 
                self.dfs_prune(coins, s+1, amount - k*c, count+k, least)
    
    def dfs_prune_boilerplate(self, coins, s, amount, count, least):
        if s >= len(coins):
            if amount == 0:
                least[0] = min(least[0], count)
            return
        c = coins[s]
        for k in range(amount // c, -1, -1):
            if count + k >= least[0]:
                break
            self.dfs_prune_boilerplate(coins, s+1, amount - k*c, count+k, least)




def main():
    q = Q322()
    q.add_args([1, 2, 5], 11)
    q.add_args([1, 2, 5], 0)
    q.add_args([1, 2, 5], 53)
    q.add_args([2, 5], 1)
    q.run()


if __name__ == "__main__":
    main()
