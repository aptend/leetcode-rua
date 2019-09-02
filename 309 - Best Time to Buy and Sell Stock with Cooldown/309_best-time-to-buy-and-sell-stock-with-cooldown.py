from leeyzer import Solution, solution


class Q309(Solution):
    @solution
    def maxProfit(self, prices):
        # 20ms 93.04%
        # hold[i] means max profit until ith day when holding a stack
        # free[i] means max profit until ith day when free to buy a stock

        N = len(prices)
        MIN = float('-inf')
        hold = [0] * (N+1)
        free = hold[:]

        hold[0] = MIN
        for i in range(1, N+1):
            p = prices[i-1]
            hold[i] = max(hold[i-1], free[i-2]-p)
            free[i] = max(free[i-1], hold[i-1]+p)
        return max(hold[N], free[N])



def main():
    q = Q309()
    q.add_args([1, 2, 3, 0, 2])
    q.add_args([1, 2, 3, 4, 5])
    q.add_args([7, 5, 3, 2, 3])
    q.run()


if __name__ == "__main__":
    main()
