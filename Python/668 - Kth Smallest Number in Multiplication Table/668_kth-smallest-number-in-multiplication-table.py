from leezy import Solution, solution


class Q668(Solution):
    @solution
    def findKthNumber(self, m, n, k):
        lo, hi = 1, m*n
        while lo <= hi:
            x = lo + (hi - lo) // 2
            le = 0
            for i in range(1, m+1):
                le += min(x // i, n)
                if le == 0 or le >= k:
                    break
            if le >= k:
                hi = x - 1
            else:
                lo = x + 1
        return lo


def main():
    q = Q668()
    q.add_args(2, 3, 6)
    q.add_args(3, 3, 5)
    q.add_args(3, 3, 3)
    q.add_args(3, 3, 1)
    q.run()


if __name__ == "__main__":
    main()
