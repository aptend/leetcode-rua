from leezy import solution, Solution


class Q233(Solution):
    @solution
    def countDigitOne(self, n):
        # 20 ms 97.37%
        width = len(str(n))
        dp = [0] * width
        for i in range(1, width):
            dp[i] = 10 ** (i-1) + dp[i-1] * 10

        def count(k):
            if k < 10:
                return int(k >= 1)
            sub_width = len(str(k)) - 1
            gap = 10 ** sub_width
            high_digit, r = divmod(k, gap)
            if high_digit == 1:
                return dp[sub_width] + r + 1 + count(r)
            else:
                return gap + high_digit * dp[sub_width] + count(r)

        return count(n)


def main():
    q = Q233()
    q.add_case(q.case(13).assert_equal(6))
    q.add_case(q.case(23).assert_equal(13))
    q.add_case(q.case(1132).assert_equal(500))
    q.run()


if __name__ == '__main__':
    main()
