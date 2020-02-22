from leezy import solution, Solution


class Q191(Solution):
    @solution
    def hammingWeight(self, n):
        ans = 0
        mask = 0xFFFFFFFF
        while n != 0:
            ans += 1
            n = n & (n-1) & mask
        return ans


def main():
    q = Q191()
    q.add_case(q.case(11).assert_equal(3))
    q.add_case(q.case(-1).assert_equal(32))
    q.add_case(q.case(-3).assert_equal(31))
    q.run()


if __name__ == '__main__':
    main()
