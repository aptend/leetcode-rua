from leezy import Solution, solution


class Q790(Solution):
    @solution
    def numTilings(self, N):
        # 20ms 70%
        if N == 1:
            return 1
        elif N == 2:
            return 2
        # dp[0]: of two blocks in the column, only top block is coverd
        # dp[1]: only bottom block is coverd
        # dp[2]: both blocks are coverd
        # dp1: previous 1st column
        # dp2: previous 2nd column
        dp0 = [0, 0, 1]
        dp1 = [1, 1, 2]
        for _ in range(N-2):
            new_dp1 = [           #            XX
                dp1[1] + dp0[2],  # use XX and X     X
                dp1[0] + dp0[2],  #     use XX and   XX
                sum(dp1) + dp0[2] # use XX   X  X  and two XXs
            ]                     #      X  XX  X
            dp0 = dp1
            dp1 = new_dp1
        return dp1[2] % (10**9 + 7)


def main():
    q = Q790()
    q.add_args(3)
    q.add_args(4)
    q.add_args(5)
    q.add_args(28)
    q.run()


if __name__ == "__main__":
    main()
