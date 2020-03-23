from leezy import solution, Solution


class Q1387(Solution):
    @solution
    def getKth(self, lo, hi, k):
        # 196 ms faster than 74.55%
        memo = {}
        def weight(x):
            if x == 1 or x == 2:
                return x - 1
            if x in memo:
                return memo[x]
            if x % 2 == 0:
                w = 1 + weight(x // 2)
            else:
                w = 1 + weight(3 * x + 1)
            memo[x] = w
            return w
        weights = [weight(x) for x in range(lo, hi+1)]
        idx = sorted(list(range(hi-lo+1)), key=lambda i: weights[i])
        return lo + idx[k-1]


def main():
    q = Q1387()
    q.add_case(q.case(12, 15, 2).assert_equal(13))
    q.add_case(q.case(1, 1, 1).assert_equal(1))
    q.add_case(q.case(7, 11, 4).assert_equal(7))
    q.add_case(q.case(10, 20, 5).assert_equal(13))
    q.add_case(q.case(1, 1000, 777).assert_equal(570))
    q.run()


if __name__ == '__main__':
    main()
