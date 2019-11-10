from leezy import Solution, solution


class Q1218(Solution):
    @solution
    def longestSubsequence(self, arr, difference):
        # 732ms 70.12%
        dp = defaultdict(int)
        g_max = 0
        for x in arr:
            dp[x] = dp[x - difference] + 1
            g_max = max(g_max, dp[x])
        return g_max


def main():
    q = Q1218()
    q.add_args([1, 2, 3, 4], 1)
    q.run()


if __name__ == "__main__":
    main()
