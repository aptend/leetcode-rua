from leezy import Solution, solution


class Q1013(Solution):
    @solution
    def canThreePartsEqualSum(self, A):
        # 288ms 53.27%
        N = len(A)
        B = [0] * (N+1)
        for i, x in enumerate(A, 1):
            B[i] = B[i-1] + x

        if B[-1] % 3 != 0:
            return False
        target = B[-1] // 3
        # use 372 is subsequence
        iterB = iter(B[1:])
        _ = all(t in iterB for t in (target, target*2))
        try:
            next(iterB)
        except StopIteration:
            return False
        else:
            return True

    @solution
    def can_three_plain(self, A):
        s, r = divmod(sum(A), 3)
        if r != 0:
            return False
        N = len(A)
        i = 0
        for _ in range(2):
            acc = A[i]  # non-empty part
            i += 1
            while i < N and acc != s:
                acc += A[i]
                i += 1
            if i == N:
                return False
        return True


def main():
    q = Q1013()
    q.add_case(q.case([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]).assert_equal(True))
    q.add_case(q.case([0, 2, 1, -6, 6, -7, 9, -1, 2, 0, 1]).assert_equal(False))
    q.add_case(q.case([3, 3, 6, 5, -2, 2, 5, 1, -9, 4]).assert_equal(True))
    q.add_case(q.case([1, -1, 1, -1]).assert_equal(False))
    q.add_case(q.case([1, 1, 1]).assert_equal(True))
    q.run()


if __name__ == "__main__":
    main()
