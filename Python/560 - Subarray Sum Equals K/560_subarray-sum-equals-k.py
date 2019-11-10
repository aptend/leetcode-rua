from leezy import Solution, solution
from collections import defaultdict

class Q560(Solution):
    @solution
    def subarraySum(self, nums, k):
        # 96ms 63.62%
        prefix_sum_occur_cnt = defaultdict(int)
        prefix_sum_occur_cnt[0] += 1
        ans = 0
        accum = 0
        for x in nums:
            accum += x
            # how many subarrays that sum up to k and ends up at x
            ans += prefix_sum_occur_cnt[accum-k]
            # maybe x is negative, prefix_sum can occur more than once.
            prefix_sum_occur_cnt[accum] += 1
        return ans


def main():
    q = Q560()
    q.add_args([1, 1, 1], 2)
    q.add_args([1, 1, -1, 1], 1)
    q.run()


if __name__ == "__main__":
    main()
