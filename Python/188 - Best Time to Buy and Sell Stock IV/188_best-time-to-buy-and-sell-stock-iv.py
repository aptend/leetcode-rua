from leezy import solution, Solution


class Q188(Solution):

    def up_segments(self, prices):
        valley = prices[0]
        prev = prices[0]
        up_segments = []
        for x in prices[1:]:
            if valley is not None:  # we are increasing
                if x < prev:  # find a peak
                    up_segments.append(prev - valley)
                    valley = None
            else:  # we are decreasing
                if x > prev:  # find a valley
                    valley = prev
            prev = x
        if valley is not None:
            up_segments.append(prices[-1] - valley)

        return (len(up_segments), sum(up_segments))

    @solution
    def maxProfit(self, k, prices):
        # 108 ms faster than 65.91%
        if not prices:
            return 0
        MIN = float('-inf')
        K = k
        max_k, sum_ = self.up_segments(prices)
        # important! avoid TLE for k = 10e9, len(prices) = 100000
        if K >= max_k:
            return sum_

        # dp[k][0]: max profit we can earn, when we hold no stock and did at most k rounds of 'buy and sell' at previous day
        # dp[k][0]: max profit we can earn, when we hold stock and did at most k rounds of 'buy and sell' at previous day
        dp = [[0, MIN] for _ in range(K+1)]
        new_dp = [[0, 0] for _ in range(K+1)]
        for p in prices:
            new_dp[0][0] = 0
            new_dp[0][1] = max(dp[0][1], dp[0][0] - p)
            for k in range(1, K+1):
                new_dp[k][0] = max(dp[k][0], dp[k-1][1] + p)
                new_dp[k][1] = max(dp[k][1], dp[k][0] - p)
            dp, new_dp = new_dp, dp
        return dp[K][0]



def main():
    q = Q188()
    q.add_case(q.case(2, [2, 4, 1]).assert_equal(2))
    q.add_case(q.case(2, [3, 2, 6, 5, 0, 3]).assert_equal(7))
    q.add_case(q.case(1000000000, [3, 2, 6, 5, 0, 3]).assert_equal(7))
    q.add_case(q.case(2, [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]).assert_equal(13))
    q.run()


if __name__ == '__main__':
    main()
