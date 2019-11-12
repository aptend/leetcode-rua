from leezy import solution, Solution

class Q970(Solution):
    @solution
    def powerfulIntegers(self, x, y, bound):
        # 20ms 99.84%
        A = [1]
        B = [1]
        n = x
        while 1 < n < bound:
            A.append(n)
            n *= x
        n = y
        while 1 < n < bound:
            B.append(n)
            n *= y
        ans = set()
        for a in A:
            for b in B:
                if a + b <= bound:
                    ans.add(a+b)
                else:
                    break
        return ans


def main():
    q = Q970()
    q.add_case(q.case(2, 3, 10).assert_equal({2, 3, 4, 5, 7, 9, 10}))
    q.run()

if __name__ == '__main__':
    main()
