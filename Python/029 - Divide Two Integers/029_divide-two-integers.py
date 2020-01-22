from leezy import solution, Solution


class Q029(Solution):
    @solution
    def divide(self, dividend, divisor):
        # this is not a valid solution under the restriction of 32-bit integers
        neg = (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0)
        ans = 0
        if dividend == -(2 ** 31) and divisor == -1:
            return 2 ** 31 - 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend >= divisor:
            i = 1
            while divisor << i < dividend:
                i += 1
            i -= 1
            ans += 2 ** i
            dividend -= divisor << i
        return -ans if neg else ans


def main():
    q = Q029()
    q.add_case(q.case(10, 3).assert_equal(3))
    q.add_case(q.case(-7, 3).assert_equal(-2))
    q.add_case(q.case(101, 3).assert_equal(33))
    q.add_case(q.case(42, 42).assert_equal(1))
    q.add_case(q.case(-2147483648, -1).assert_equal(2147483647))
    q.add_case(q.case(-2147483648, 1).assert_equal(-2147483648))
    q.run()

if __name__ == '__main__':
    main()
