from leezy import Solution, solution


class Q121(Solution):
    @solution
    def maxProfit(self, prices):
        # 36ms 99.56%
        if len(prices) < 2:
            return 0
        # dp means minimum price found so far
        dp = prices[0]
        ans = 0
        for x in prices[1:]:
            ans = max(ans, x - dp)
            dp = min(dp, x)
        return ans


def main():
    q = Q121()
    q.add_args([7, 1, 5, 3, 6, 4])
    q.add_args([7, 6, 5])
    q.run()


if __name__ == "__main__":
    main()
