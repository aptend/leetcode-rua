from leezy import solution, Solution
from itertools import chain
from collections import Counter


class Q1054(Solution):
    @solution
    def rearrangeBarcodes(self, barcodes):
        # 452ms 92.03%
        N = len(barcodes)
        idx = chain(range(0, N, 2), range(1, N, 2))
        counter = Counter(barcodes)
        ans = [0] * N
        for x, cnt in counter.most_common():
            for _ in range(cnt):
                ans[next(idx)] = x
        return ans


def main():
    q = Q1054()

    def check(A):
        for x, nx in zip(A, A[1:]):
            if x == nx:
                return False
        return True

    q.add_case(q.case([1, 1, 1, 2, 2, 2]).assert_true_with(check))
    q.add_case(q.case([1, 2, 2, 2, 5]).assert_true_with(check))
    q.add_case(q.case([1, 1, 1, 1, 2, 2, 3, 3]).assert_true_with(check))
    q.run()


if __name__ == '__main__':
    main()
