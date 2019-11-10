from leezy import Solution, solution


class Q312(Solution):
    @solution
    def maxCoins(self, nums):
        # 764ms 22.63%
        nums = [1] + nums + [1]
        N = len(nums)
        memo = [[None] * N for _ in range(N)]
        # memo[i][j] means max score when bursting nums[i+1:j]
        def solve(i, j):
            if j - i == 1:
                return 0
            if memo[i][j] is not None:
                return memo[i][j]
            max_ = 0
            for k in range(i+1, j):
                max_ = max(max_, solve(i, k) + solve(k, j) + nums[i]*nums[k]*nums[j])
            memo[i][j] = max_
            return max_
        return solve(0, N-1)

    @solution
    def max_coins(self, nums):
        # 436ms 69.05%
        nums = [1] + nums + [1]
        N = len(nums)
        dp = [[0] * N for _ in range(N)]
        # dp[i][j] means max score when bursting nums[i+1:j]
        # nums[i]、nums[j] are sentinel values
        for l in range(1, len(nums)):
            for i in range(0, N-l):
                j = i + l
                for k in range(i+1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i]*nums[k]*nums[j])
        return dp[0][N-1]





def main():
    q = Q312()
    q.add_args([2, 3])
    q.add_args([3, 4, 5])
    q.add_args([3, 1, 5, 8])
    q.run()


if __name__ == "__main__":
    main()
