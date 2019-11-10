from leezy import Solution, solution


class Q1191(Solution):
    @solution
    def kConcatenationMaxSum(self, arr, k):
        # 400ms 73.63%
        g_max = 0
        dp = 0
        for x in arr:
            dp = max(x, dp+x)
            g_max = max(dp, g_max)
        max_ee = max(dp, 0)
        dp = 0
        for x in reversed(arr):
            dp = max(x, dp+x)
        max_ss = max(dp, 0)

        _sum = max(0, sum(arr))
        g_max = max(_sum, g_max)

        if k >= 2:
            concat_sum = max_ee + max_ss
            for _ in range(k-2):
                concat_sum += _sum
            g_max = max(g_max, concat_sum % (10**9+7))
        return g_max




def main():
    q = Q1191()
    q.add_args([1, 2], 3)
    q.add_args([-1, -2], 3)
    q.add_args([-2, -5, 0, 0, 9, 3, -5, -2, 4], 5)
    q.run()


if __name__ == "__main__":
    main()
