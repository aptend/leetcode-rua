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
    
    @solution
    def is_monotonic(self, A):
        # 524ms 80.93%
        return all(x <= y for x, y in zip(A, A[1:])) or all(x >= y for x, y in zip(A, A[1:]))


def main():
    q = Q896()
    q.add_case(q.case([1, 2, 2, 3]).assert_equal(True))
    q.add_case(q.case([1, 1, 1]).assert_equal(True))
    q.add_case(q.case([1, 2, 1, 3]).assert_equal(False))
    q.add_case(q.case([5, 4, 2, 2]).assert_equal(True))
    q.run()


if __name__ == "__main__":
    main()
