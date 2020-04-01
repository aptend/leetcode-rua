from leezy import solution, Solution


class Q1395(Solution):
    @solution
    def numTeams(self, rating):
        ans = 0
        A = rating
        N = len(A)
        bigger = [0] * N
        smaller = [0] * N
        for i in range(N):
            for j in range(i+1, N):
                if A[i] < A[j]:
                    bigger[i] += 1
                else:
                    smaller[i] += 1
        for i in range(N):
            for j in range(i+1, N):
                if A[i] > A[j]:
                    ans += smaller[j]
                else:
                    ans += bigger[j]
        return ans


def main():
    q = Q1395()
    q.add_case(q.case([2, 5, 3, 4, 1]).assert_equal(3))
    q.add_case(q.case([2, 1, 3]).assert_equal(0))
    q.add_case(q.case([1, 2, 3, 4]).assert_equal(4))
    q.run()


if __name__ == '__main__':
    main()
