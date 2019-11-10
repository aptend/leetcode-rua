from leezy import Solution, solution


class Q786(Solution):
    @solution
    def kthSmallestPrimeFraction(self, A, K):
        # 148ms 96.3%
        N = len(A)
        lo, hi = 0.0, 1.0
        while lo <= hi:
            m = (lo + hi) / 2
            le = 0
            max_, p, q = 0.0, -1, -1
            i, j = 0, 1
            for i in range(N-1):
                while j < N and A[i] > m * A[j]:
                    j += 1
                if j == N:
                    break
                le += N - j
                f = A[i] / A[j]
                if f > max_:
                    max_ = f
                    p = i
                    q = j
            if le == K:
                return [A[p], A[q]]
            elif le > K:
                hi = m
            else:
                lo = m
        return [-1, -1]


"""
      1     2    3   4
0    1/3  1/5  1/7 1/11
1         3/5  3/7 3/11
2              5/7 5/11
3                  7/11
"""

def main():
    q = Q786()
    q.add_args([1, 2, 3, 5], 3)
    q.add_args([1, 7], 1)
    q.run()


if __name__ == "__main__":
    main()
