from leeyzer import Solution, solution
from collections import defaultdict

class Q560(Solution):
    @solution
    def subarraySum(self, nums, k):
        # 96ms 63.62%
        head_based_sum = defaultdict(int)
        head_based_sum[0] += 1
        ans = 0
        accum = 0
        for x in nums:
            accum += x
            ans += head_based_sum[accum-k]
            head_based_sum[accum] += 1
        return ans


def main():
    q = Q560()
    q.add_args([1, 1, 1], 2)
    q.add_args([1, 1, -1, 1], 1)
    q.run()


if __name__ == "__main__":
    main()
