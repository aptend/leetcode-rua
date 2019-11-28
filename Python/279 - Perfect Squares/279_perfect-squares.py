from leezy import solution, Solution


class Q279(Solution):
    @solution
    def numSquares(self, n):
        # 5260ms 5%
        candids = []
        x = 1
        while x * x <= n:
            candids.append(x * x)
            x += 1
        N = len(candids)
        dp = [0, 1]
        for x in range(2, n+1):
            j = 0
            min_n = float('inf')
            while j < N and candids[j] <= x:
                min_n = min(min_n, dp[x-candids[j]]+1)
                j += 1
            dp.append(min_n)
        return dp[n]
    
    @solution
    def square_concise(self, n):
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        for i in range(1, n+1):
            j = 1
            while j ** 2 <= i:
                dp[i] = min(dp[i], dp[i-j**2] + 1)
                j += 1
        return dp[n]


def main():
    q = Q279()
    q.add_case(q.case(4).assert_equal(1))
    q.add_case(q.case(12).assert_equal(3))
    q.add_case(q.case(13).assert_equal(2))
    q.run()

if __name__ == '__main__':
    main()
