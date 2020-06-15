from leezy import solution, Solution


class Q1482(Solution):
    @solution
    def minDays(self, bloomDay, m, k):
        if len(bloomDay) < m * k:
            return -1

        def check(x):
            n_complete = 0
            count = 0
            for d in bloomDay:
                if x >= d:
                    count += 1
                    if count >= k:
                        n_complete += 1
                        count = 0
                        if n_complete >= m:
                            return True
                else:
                    count = 0
            return False

        lo, hi = 0, max(bloomDay)
        while lo <= hi:
            mid = (lo + hi) // 2
            if check(mid):
                hi = mid - 1
            else:
                lo = mid + 1
        return lo


def main():
    q = Q1482()
    q.add_case(q.case([1, 10, 3, 10, 2], 3, 1).assert_equal(3))
    q.add_case(q.case([1, 10, 3, 10, 2], 3, 2).assert_equal(-1))
    q.add_case(q.case([1, 10, 3, 10, 2], 2, 2).assert_equal(10))
    q.add_case(q.case([1, 2, 4, 9, 3, 4, 1], 2, 2).assert_equal(4))
    q.add_case(q.case([7, 7, 7, 7, 12, 7, 7], 2, 3).assert_equal(12))
    q.add_case(q.case([1000000000, 1000000000], 1, 1).assert_equal(1000000000))
    q.add_case(q.case([1, 10, 2, 9, 3, 8, 4, 7, 5, 6], 4, 2).assert_equal(9))
    q.run()


if __name__ == '__main__':
    main()
