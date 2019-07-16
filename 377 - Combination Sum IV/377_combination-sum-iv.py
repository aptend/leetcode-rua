from leeyzer import Solution, solution


class Q377(Solution):
    """my thoughts for the follow up question is stopping recursion when
     target is less than -(the max sum that nums can sum up to).
    """
    @solution
    def combinationSum4(self, nums, target):
        memo = {}
        nums = sorted(nums)
        return self.soln(nums, target, memo)

    def soln(self, nums, target, memo):
        if target == 0:
            return 1
        if target in memo:
            return memo[target]
        total = 0
        for n in nums:
            if n > target:
                break
            total += self.soln(nums, target - n, memo)
        memo[target] = total
        return total

    @solution
    def combination_sum(self, nums, target):
        if target < 0:
            return 0
        # dp[i]: how many ways to sum up to target using nums
        dp = [1] + [0]*target
        for i in range(1, target+1):
            for n in nums:
                if n <= target:
                    dp[i] += dp[i - n]
        return dp[target]


def main():
    q = Q377()
    q.add_args([1, 2, 3], 4)
    q.add_args([1, 2, 3], 0)
    q.add_args([1, 2, 3], -1)
    q.add_args([5, 2, 3], 1)
    q.add_args([1, 2, 5], 5)
    q.run()


if __name__ == "__main__":
    main()
