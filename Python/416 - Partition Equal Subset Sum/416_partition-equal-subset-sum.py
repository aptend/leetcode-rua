from leeyzer import Solution, solution


class Q416(Solution):
    @solution
    def canPartition(self, nums):
        # see 494. target sum for more infomation
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        dp = [False] * (target+1)
        dp[0] = True
        for n in nums:
            for i in range(target, n-1, -1):
                dp[i] |= dp[i-n]
        return dp[target]


def main():
    q = Q416()
    q.add_args([1, 5, 11, 5])
    q.add_args([1, 2, 3, 5])
    q.run()


if __name__ == "__main__":
    main()
