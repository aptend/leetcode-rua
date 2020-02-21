from leezy import solution, Solution


class Q054(Solution):
    @solution
    def spiralOrder(self, matrix):
        # 28ms 98.89%
        if len(matrix) == 0:
            return []
        m, n = len(matrix), len(matrix[0])
        total = n
        ans = matrix[0][:]
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
                    ans.append(matrix[i][j])
                    total += 1
                if total == N:
                    break
        return ans

    @solution
    def spiral(self, A):
        if len(A) == 0:
            return []
        m, n = len(A), len(A[0])
        i, j = 0, 0
        ans = []
        while m > 1 and n > 1:
            for k in range(j, j+n-1):
                ans.append(A[i][k])
            for k in range(i, i+m-1):
                ans.append(A[k][j+n-1])
            for k in range(j+n-1, j, -1):
                ans.append(A[i+m-1][k])
            for k in range(i+m-1, i, -1):
                ans.append(A[k][j])
            m -= 2
            n -= 2
            i += 1
            j += 1
        if m == 1:
            for k in range(j, j+n):
                ans.append(A[i][k])
        elif n == 1:
            for k in range(i, i+m):
                ans.append(A[k][j])
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
