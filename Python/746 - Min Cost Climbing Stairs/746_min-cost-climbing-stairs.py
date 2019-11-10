from leezy import Solution, solution


class Q746(Solution):
    @solution
    def minCostClimbingStairs(self, cost):
        # 32ms 99.23%
        dp0, dp1 = cost[0], cost[1]
        for c in cost[2:]:
            dp0, dp1 = dp1, min(dp0, dp1) + c
        return min(dp0, dp1)


def main():
    q = Q746()
    q.add_args([0, 0, 0, 0])
    q.add_args([10, 15, 20])
    q.add_args([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
    q.run()


if __name__ == "__main__":
    main()
