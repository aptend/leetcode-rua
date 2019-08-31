from leeyzer import Solution, solution


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
        iterB = iter(B)
        return all(t in iterB for t in (target, target*2))


def main():
    q = Q1013()
    q.add_args([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1])
    q.run()


if __name__ == "__main__":
    main()
