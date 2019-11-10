from leezy import Solution, solution


class Q070(Solution):
    @solution
    def climbStairs(self, n):
        # 12ms 89.86%
        dp0, dp1 = 1, 1
        for _ in range(2, n+1):
            dp0, dp1 = dp1, dp0 + dp1
        return dp1


def main():
    q = Q070()
    q.add_args(2)
    q.add_args(3)
    q.add_args(5)
    q.run()


if __name__ == "__main__":
    main()
