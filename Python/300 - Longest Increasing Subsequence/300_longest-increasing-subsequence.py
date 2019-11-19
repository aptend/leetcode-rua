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
        # 36ms 99.25%
        # i was inspired by the queue-based solution of
        # 995 - Minimum Number of K Consecutive Bit Flips
        increasing_list = []
        for x in nums:
            idx = bisect_left(increasing_list, x)
            if idx == len(increasing_list):
                increasing_list.append(x)
            else:
                # it is a bit greedy. if we want the list to be longer,
                # try our best to hold `sum(list)` smallest
                increasing_list[idx] = x
        return len(increasing_list)


def main():
    q = Q300()
    q.add_case(q.case([]).assert_equal(0))
    q.add_case(q.case([2, 2, 2]).assert_equal(1))
    q.add_case(q.case([10, 9, 2, 5, 3, 7, 101, 18]).assert_equal(4))
    q.add_case(q.case([1, 3, 6, 7, 9, 4, 10, 5, 6]).assert_equal(6))
    q.run()


if __name__ == "__main__":
    main()
