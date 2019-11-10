from leezy import Solution, solution


class Q852(Solution):
    @solution
    def peakIndexInMountainArray(self, A):
        # 48ms 99.80%
        lo, hi = 0, len(A)-1
        while lo <= hi:
            m = lo + (hi - lo) // 2
            if A[m] > A[m+1]:
                hi = m - 1
            else:
                lo = m + 1
        return lo

def main():
    q = Q852()
    q.add_args([0, 1, 0])
    q.add_args([0, 2, 1, 0])
    q.run()


if __name__ == "__main__":
    main()
