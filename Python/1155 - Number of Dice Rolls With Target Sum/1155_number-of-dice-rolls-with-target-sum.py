from leezy import Solution, solution


class Q1155(Solution):
    @solution
    def numRollsToTarget(self, d, f, target):
        # 484ms 56.9%
        # compare with 518 coin change ii
        dp = [0] * (target+1)
        dp[0] = 1
        for _ in range(d):
            new_dp = [0] * (target + 1)
            for i in range(1, f+1):
                for t in range(i, target+1):
                    new_dp[t] += dp[t-i]
            dp = new_dp
        return dp[target] % (10**9 + 7)


def main():
    q = Q1155()
    q.add_args(2, 6, 2) # 1
    q.add_args(3, 5, 7) # 15
    q.run()


if __name__ == "__main__":
    main()
