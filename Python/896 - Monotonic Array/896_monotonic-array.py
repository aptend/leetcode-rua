from leezy import Solution, solution


class Q896(Solution):
    @solution
    def isMonotonic(self, A):
        # 560ms 59.47%
        N = len(A)
        for i in range(1, N):
            if A[i] < A[i-1]:
                while i < N and A[i] <= A[i-1]:
                    i += 1
                return i == N
            elif A[i] > A[i-1]:
                while i < N and A[i] >= A[i-1]:
                    i += 1
                return i == N
        return True


def main():
    q = Q896()
    q.add_args([1, 2, 2, 3])
    q.run()


if __name__ == "__main__":
    main()
