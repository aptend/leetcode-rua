from leezy import solution, Solution


class Q287(Solution):
    @solution
    def findDuplicate(self, nums):
        lo, hi = 1, len(nums)-1
        while lo <= hi:
            mid = (lo + hi) // 2
            cnt = len([x for x in nums if x <= mid])
            if cnt > mid:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo


def main():
    q = Q287()
    q.add_case(q.case([1, 3, 4, 2, 2]).assert_equal(2))
    q.add_case(q.case([3, 1, 3, 4, 2]).assert_equal(3))
    q.add_case(q.case([4, 1, 4, 4, 2]).assert_equal(4))
    q.run()

if __name__ == '__main__':
    main()
