from leezy import solution, Solution


class Q050(Solution):
    """
    the recursive and iterative solutions are like what happens in merge sort
    """
    @solution
    def myPow(self, x, n):
        # 20ms 96.71%
        if n == 0:
            return 1
        in_x = x
        # cast n from i32 to i64, and no need to handle -2**31
        if n < 0:
            in_x = 1 / x
            n = -n
        memo = {}

        def inner_pow(n):
            if n == 1:
                return in_x
            if n in memo:
                return memo[n]
            half, r = divmod(n, 2)
            res = inner_pow(half) * inner_pow(half)
            if r == 1:
                res *= in_x
            memo[n] = res
            return res
        return inner_pow(n)

    @solution
    def iter_pow(self, x, n):
        # 28ms 67.67%
        if n == 0:
            return 1

        if n < 0:
            x = 1 / x
            n = -n

        parts = [x]
        i = 0
        ans = 1
        while (1 << i) <= n:
            parts.append(parts[-1]*parts[-1])
            if (n >> i) & 0x1:
                ans *= parts[i]
            i += 1
        return ans


def main():
    q = Q050()
    q.add_case(q.case(2.0, 10).assert_equal(1024))
    q.add_case(q.case(2.0, -2).assert_equal(0.25))
    q.add_case(q.case(2.0, 7).assert_equal(128))
    q.add_case(q.case(2.1, 3)
                .assert_true_with(lambda x: abs(x - 9.261) < 0.0000001))
    q.run()


if __name__ == '__main__':
    main()
