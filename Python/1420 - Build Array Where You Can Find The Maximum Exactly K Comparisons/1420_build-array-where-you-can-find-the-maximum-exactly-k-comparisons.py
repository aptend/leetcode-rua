from leezy import solution, Solution
from functools import lru_cache


class Q1420(Solution):
    @solution
    def numOfArrays(self, n, m, k):
        kmod = 10**9 + 7
        # pull
        @lru_cache(maxsize=None)
        def dp(i, largest, cost):
            if i == 1:
                return 1 if cost == 1 else 0
            if cost <= 0 or largest < cost:
                return 0

            ans = dp(i-1, largest, cost) * largest % kmod
            for smaller_largest in range(1, largest):
                ans += dp(i-1, smaller_largest, cost-1)
            return ans % kmod
        return sum(dp(n, maximum, k) for maximum in range(1, m+1)) % kmod

    def num_arrays(self, n, m, k):
        # TODO: push
        pass


def main():
    q = Q1420()
    q.add_case(q.case(2, 3, 1).assert_equal(6))
    q.add_case(q.case(n=5, m=2, k=3).assert_equal(0))
    q.add_case(q.case(n=9, m=1, k=1).assert_equal(1))
    q.add_case(q.case(n=50, m=100, k=25).assert_equal(34549172))
    q.add_case(q.case(n=37, m=17, k=7).assert_equal(418930126))
    q.run()


if __name__ == '__main__':
    main()
