from leeyzer import Solution, solution


class Q1220(Solution):
    @solution
    def countVowelPermutation(self, n):
        # 248ms 64.11%
        a, e, i, o, u = 0, 1, 2, 3, 4
        dp = [1] * 5
        new_dp = [0] * 5
        for _ in range(n-1):
            new_dp[a] = dp[e] + dp[u] + dp[i]
            new_dp[e] = dp[a] + dp[i]
            new_dp[i] = dp[e] + dp[o]
            new_dp[o] = dp[i]
            new_dp[u] = dp[i] + dp[o]
            dp, new_dp = new_dp, dp
        return sum(dp) % (10 ** 9 + 7)


def main():
    q = Q1220()
    q.add_args(1)
    q.run()


if __name__ == "__main__":
    main()
