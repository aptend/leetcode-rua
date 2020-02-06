from leezy import solution, Solution


class Q858(Solution):
    @solution
    def mirrorReflection(self, p, q):
        def gcd(p, q):
            while q:
                p, q = q, p % q
            return p

        up = p * q // gcd(p, q)
        if (up // p) % 2 == 0:
            return 0
        elif (up // q) % 2 == 0:
            return 2
        else:
            return 1


def main():
    q = Q858()
    q.add_case(q.case(2, 1).assert_equal(2))
    q.add_case(q.case(3, 1).assert_equal(1))
    q.add_case(q.case(3, 2).assert_equal(0))
    q.run()

if __name__ == '__main__':
    main()
