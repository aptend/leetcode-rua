from leezy import Solution, solution


class Q213(Solution):
    @solution
    def rob(self, nums):
        # 8ms 99.12%
        def _rob(lo, hi):
            # refer to 198 House Robber
            dp0 = dp1 = 0
            for n in nums[lo:hi+1]:
                new_dp0 = max(dp0, dp1)
                dp1 = dp0 + n
                dp0 = new_dp0
            return max(dp0, dp1)
        N = len(nums)
        if N == 1:
            return nums[0]
        return max(_rob(1, N-1), _rob(0, N-2))


def main():
    q = Q213()
    q.add_args([2, 3, 2])
    q.add_args([1, 2, 3, 1])
    q.run()


if __name__ == "__main__":
    main()
