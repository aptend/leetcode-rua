from leezy import Solution, solution


class Q714(Solution):
    @solution
    def maxProfit(self, prices, fee):
        # 708 ms, 29.27%
        N = len(prices)
        MIN = float('-inf')
        hold = [0] * (N+1)
        free = hold[:]

        hold[0] = MIN
        for i in range(1, N+1):
            p = prices[i-1]
            hold[i] = max(hold[i-1], free[i-1]-p-fee)
            free[i] = max(free[i-1], hold[i-1]+p)
        return max(hold[N], free[N])
    
    @solution
    def max_profit(self, prices, fee):
        # 644ms 69.45%
        N = len(prices)
        MIN = float('-inf')
        hold, free = MIN, 0
        for i in range(N):
            p = prices[i]
            hold, free = max(hold, free - p - fee), max(free, hold + p)
        return max(hold, free)


def main():
    q = Q714()
    q.add_args([1, 3, 2, 8, 4, 9], 2) # 8
    q.add_args([4, 11, 4, 1, 19], 2) # 21
    q.run()


if __name__ == "__main__":
    main()
