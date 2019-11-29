from leezy import solution, Solution


class Q166(Solution):
    @solution
    def fractionToDecimal(self, numerator, denominator):
        n, d = numerator, denominator
        if d == 0:
            return "NaN"
        flag = '-' if n*d < 0 else ''
        n, d = abs(n), abs(d)
        x, n = divmod(n, d)
        if n == 0:
            return flag + str(x)
        ans = []
        n_sets = dict()
        ans.append(str(x))
        ans.append(".")
        while n and n not in n_sets:
            n_sets[n] = len(ans)
            x, n = divmod(n*10, d)
            ans.append(str(x))
        if n > 0:
            ans.insert(n_sets[n], "(")
            ans.append(')')
        return flag + ''.join(ans)


def main():
    q = Q166()
    q.add_case(q.case(1, -2).assert_equal("-0.5"))
    q.add_case(q.case(2, 1).assert_equal("2"))
    q.add_case(q.case(2, 3).assert_equal("0.(6)"))
    q.add_case(q.case(10001, 300).assert_equal("33.33(6)"))
    q.add_case(q.case(1, 73).assert_equal("0.(01369863)"))
    q.run()


if __name__ == '__main__':
    main()
