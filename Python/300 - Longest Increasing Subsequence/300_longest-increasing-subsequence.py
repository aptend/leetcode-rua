from leezy import Solution, solution
from bisect import bisect_left

class Q300(Solution):
    @solution
    def lengthOfLIS(self, nums):
        # O(n^2) 828ms 59.76%
        if not nums:
            return 0
        N = len(nums)
        # dp[i] means max length among all subsequences ending with nums[i]
        dp = [1 for _ in range(N)]
        for i in range(N):
            for j in range(i):
                if nums[j] < nums[i] and dp[j] >= dp[i]:
                    dp[i] = dp[j]+1
        return max(dp)

    @solution
    def length_of_LIS_better(self, nums):
        pass
        # to be continued




def main():
    q = Q300()
    # q.add_args([])
    # q.add_args([2, 2, 2])
    # q.add_args([10, 9, 2, 5, 3, 7, 101, 18])
    q.add_args([1, 3, 6, 7, 9, 4, 10, 5, 6])
    q.run()


if __name__ == "__main__":
    main()
