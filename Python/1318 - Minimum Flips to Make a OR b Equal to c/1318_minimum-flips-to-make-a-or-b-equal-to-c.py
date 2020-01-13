from leezy import solution, Solution


class Q1318(Solution):
    @solution
    def minFlips(self, a, b, c):
        ans = 0
        mask = 0x1
        for i in range(31):
            sa, sb, sc = (a >> i) & mask, (b >> i) & mask, (c >> i) & mask
            if sc:
                if sa == 0 and sb == 0:
                    ans += 1
            else:
                ans += sa + sb
        return ans


def main():
    q = Q1318()
    q.add_case(q.case(2, 6, 5).assert_equal(3))
    q.add_case(q.case(a=4, b=2, c=7).assert_equal(1))
    q.add_case(q.case(a=1, b=2, c=3).assert_equal(0))
    q.run()

if __name__ == '__main__':
    main()
