from leeyzer import Solution, solution


class Q474(Solution):
    @solution
    def findMaxForm(self, strs, m, n):
        # 2872ms 67.91%
        # zero-one knapsack problem, reverse the order to reduce dimension
        # dp[i][j] means maximum strings we can cover, 
        # when it's allowed to hold up to i zeros and j ones
        dp = [[0] * (n+1) for _ in range(m+1)]
        for s in strs:
            o = s.count('1')
            z = s.count('0')
            for i in range(m, z-1, -1):
                for j in range(n, o-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-z][j-o]+1)
        return dp[m][n]




def main():
    q = Q474()
    q.add_args(['10', '0001', '111001', '1', '0'], 5, 3)
    q.add_args(["10", "0", "1"], 1, 1)
    q.run()


if __name__ == "__main__":
    main()
