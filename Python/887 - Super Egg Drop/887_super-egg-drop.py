from leezy import solution, Solution

class Q887(Solution):
    @solution
    def superEggDrop(self, K, N):
        #TLE passed cases:  62/121
        memo = {}
        def dp(k, n):
            if k == 1:
                return n
            if n <= 1:
                return n
            if k <= 0:
                return 0
            save = memo.get((k,n), None)
            if save:
                return save
            save = 1 + min(max(dp(k-1, m-1), dp(k, n-m)) for m in range(1, n+1))
            memo[(k, n)] = save
            return save
        return dp(K, N)
    
    @solution
    def super_egg_drop(self, K, N):
        # 2312ms, 14.17%
        memo = {}
        def dp(k, n):
            if k == 1:
                return n
            if n <= 1:
                return n
            if k <= 0:
                return 0
            save = memo.get((k, n), None)
            if save:
                return save
            # we use binary search to find max(dp(k-1, m), dp(k, n-m))
            # dp(k-1, m) increases with m
            # dp(k, n-m) decreases with m
            # so dp(k-1, m) - dp(k, n-m) is increasing
            # and the zero-closest position is what we want
            lo, hi = 1, n+1
            while lo <= hi:
                m = lo + (hi - lo) // 2
                if dp(k-1, m-1) - dp(k, n-m) >= 0:
                    hi = m - 1
                else:
                    lo = m + 1
            save = 1 + max(dp(k-1, lo-1), dp(k, n-lo))
            memo[(k, n)] = save
            return save
        return dp(K, N)


def main():
    q = Q887()
    q.add_case(q.case(1, 2).assert_equal(2))
    q.add_case(q.case(2, 3).assert_equal(2))
    q.add_case(q.case(2, 6).assert_equal(3))
    q.add_case(q.case(2, 100).assert_equal(14))
    q.add_case(q.case(3, 14).assert_equal(4))
    q.add_case(q.case(4, 87).assert_equal(7))
    q.add_case(q.case(99, 5).assert_equal(3))
    q.run()


if __name__ == '__main__':
    main()
