from leezy import solution, Solution


class Q054(Solution):
    @solution
    def spiralOrder(self, Arix):
        # 28ms 98.89%
        if len(Arix) == 0:
            return []
        m, n = len(Arix), len(Arix[0])
        total = n
        ans = Arix[0][:]
        dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        i, j = 0, n-1
        k = 0
        N = m * n
        while total < N:
            for idx, (di, dj) in enumerate(dirs):
                if idx == 0 or idx == 2:
                    k += 1
                if idx % 2 == 0:
                    cnt = m - k
                else:
                    cnt = n - k
                for _ in range(cnt):
                    i, j = i+di, j+dj
                    ans.append(Arix[i][j])
                    total += 1
                if total == N:
                    break
        return ans

    @solution
    def spiral(self, A):
        if not A or len(A) == 0:
            return []
        n, m = len(A), len(A[0])
        i = j = 0
        ans = []
        while n > 1 and m > 1:
            ans.extend(A[i][k] for k in range(j, j+m))  # m
            ans.extend(A[k][j+m-1] for k in range(i+1, i+1+n-1))  # n-1
            ans.extend(A[i+n-1][k] for k in reversed(range(j, j+m-1)))  # m-1
            ans.extend(A[k][j] for k in reversed(range(i+1, i+1+n-2)))  # n-2
            i += 1
            j += 1
            n -= 2
            m -= 2
        if n == 1:
            ans.extend(A[i][k] for k in range(j, j+m))
        elif m == 1:  # 不要写成else
            ans.extend(A[k][j] for k in range(i, i+n))
        return ans


def main():
    q = Q054()
    q.add_case(q.case([[7], [9], [6]])
                .assert_equal([7, 9, 6]))
    q.add_case(q.case([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
                .assert_equal([1, 2, 3, 6, 9, 8, 7, 4, 5]))
    q.add_case(q.case([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
               .assert_equal([1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]))
    q.run()


if __name__ == '__main__':
    main()
