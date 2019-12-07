from leezy import solution, Solution
from collections import Counter


class Q1007(Solution):
    @solution
    def minDominoRotations(self, A, B):
        # 1292 ms 65.01%
        Ca = Counter(A)
        Cb = Counter(B)
        s = set([A[0], B[0]])
        for p in zip(A, B):
            s &= set(p)
            if len(s) == 0:
                return -1
        ans = float('inf')
        for c in s:
            ans = min(ans, len(A) - max(Ca[c], Cb[c]))
        return ans


def main():
    q = Q1007()
    q.add_case(q.case([2, 1, 2, 4, 2, 2], [5, 2, 6, 2, 3, 2]).assert_equal(2))
    q.add_case(q.case([1], [1]).assert_equal(0))
    q.add_case(q.case([1, 2, 2, 2, 1], [2, 2, 1, 1, 2]).assert_equal(2))
    q.run()


if __name__ == '__main__':
    main()
