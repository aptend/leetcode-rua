from leezy import Solution, solution


class Q1011(Solution):
    @solution
    def shipWithinDays(self, weights, D):
        def days_needed(cap):
            k = 1
            this_ship_weight = 0
            for x in weights:
                this_ship_weight += x
                if this_ship_weight > cap:
                    this_ship_weight = x
                    k += 1
            return k
        lo, hi = max(weights), sum(weights)
        while lo <= hi:
            mid = (lo + hi) // 2
            if days_needed(mid) <= D:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo


def main():
    q = Q1011()
    q.add_case(q.case([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5).assert_equal(15))
    q.add_case(q.case([3, 2, 2, 4, 1, 4], 3).assert_equal(6))
    q.add_case(q.case([1, 2, 3, 1, 1], 4).assert_equal(3))
    q.run()


if __name__ == "__main__":
    main()
