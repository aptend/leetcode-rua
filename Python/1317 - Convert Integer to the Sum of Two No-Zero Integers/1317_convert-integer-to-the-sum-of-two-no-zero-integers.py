from leezy import solution, Solution


class Q1317(Solution):
    @solution
    def getNoZeroIntegers(self, n):
        def has_zero(k):
            while k > 0:
                k, r = divmod(k, 10)
                if r == 0:
                    return True
            return False

        for i in range(1, 10000):
            if has_zero(i) or has_zero(n-i):
                continue
            else:
                return [i, n-i]


def main():
    q = Q1317()
    q.add_case(q.case(2).assert_equal([1, 1]))
    q.add_case(q.case(1010).assert_equal([11,999]))
    q.run()

if __name__ == '__main__':
    main()
