from leezy import Solution, solution


class Q867(Solution):
    @solution
    def transpose(self, A):
        # 56ms 79.93%
        m, n = len(A), len(A[0])
        B = [[0] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                B[j][i] = A[i][j]
        return B


def main():
    q = Q867()
    q.add_args([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    q.run()


if __name__ == "__main__":
    main()
