from leezy import Solution, solution


class Q069(Solution):
    @solution
    def mySqrt(self, x):
        lo, hi = 0, x+1
        while lo < hi:
            mid = lo + (hi-lo) // 2
            if mid*mid > x:
                hi = mid
            else:
                lo = mid + 1
        return lo - 1
    
    @solution
    def sqrt(self, x):
        lo, hi = 0, x
        while lo <= hi:
            mid = (lo + hi) // 2
            if mid * mid > x:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo - 1

def main():
    q = Q069()
    q.add_args(4)
    q.add_args(8)
    q.add_args(9)
    q.add_args(122)
    q.run()


if __name__ == "__main__":
    main()
