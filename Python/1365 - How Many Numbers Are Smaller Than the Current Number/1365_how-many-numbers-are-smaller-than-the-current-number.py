from leezy import solution, Solution
from bisect import bisect_left


class Q1365(Solution):
    @solution
    def smallerNumbersThanCurrent(self, nums):
        hay = sorted(nums)
        ans = [0] * len(nums)
        for i, x in enumerate(nums):
            ans[i] = bisect_left(hay, x)
        return ans


def main():
    q = Q1365()
    q.add_case(q.case([8, 1, 2, 2, 3]).assert_equal([4, 0, 1, 1, 3]))
    q.add_case(q.case([7, 7, 7, 7, 7]).assert_equal([0, 0, 0, 0, 0]))
    q.run()


if __name__ == '__main__':
    main()
