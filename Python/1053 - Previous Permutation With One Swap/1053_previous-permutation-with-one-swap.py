from leezy import solution, Solution


class Q1053(Solution):
    @solution
    def prevPermOpt1(self, A):
        # 244ms 94.13%
        N = len(A)
        i = N-2
        while i >= 0 and A[i] <= A[i+1]:
            i -= 1

        if i == -1:
            return A

        max_ = A[i+1]
        max_idx = i+1
        for j in range(i+1, N):
            if A[j] >= A[i]:
                break
            if A[j] > max_:
                max_ = A[j]
                max_idx = j
        j = max_idx
        A[i], A[j] = A[j], A[i]
        return A


def main():
    q = Q1053()
    q.add_case(q.case([3, 2, 1]).assert_equal([3, 1, 2]))
    q.add_case(q.case([3, 1, 1, 3]).assert_equal([1, 3, 1, 3]))
    q.add_case(q.case([1, 1, 5]).assert_equal([1, 1, 5]))
    q.add_case(q.case([1, 9, 4, 6, 7]).assert_equal([1, 7, 4, 6, 9]))
    q.run()

if __name__ == '__main__':
    main()
