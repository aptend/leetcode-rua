from leeyzer import Solution, solution


class Q1201(Solution):
    @solution
    def nthUglyNumber(self, n, a, b, c):
        # 26ms
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x
        
        # lcm: least common muliple
        # gcd: greatest common divisor
        # a * b = gcd(a, b) * lcm(a, b)
        ab = a * b // gcd(a, b)
        bc = b * c // gcd(b, c)
        ac = a * c // gcd(a, c)
        abc = ab * c // gcd(ab, c)

        def small_cnt(x):
            return x // a + x // b + x // c - x // ab - x // bc - x // ac + x // abc

        lo = 1
        hi = int(2e9 + 1)
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if small_cnt(mid) >= n:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo




def main():
    q = Q1201()
    q.add_args(3, 2, 3, 5)
    q.add_args(4, 2, 3, 4)
    q.add_args(n=5, a=2, b=11, c=13)
    q.add_args(n=1000000000, a=2, b=217983653, c=336916467)
    q.add_args(3, 3, 3, 3)
    q.run()


if __name__ == "__main__":
    main()
