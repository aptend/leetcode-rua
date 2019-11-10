from leezy import Solution, solution


class Q052(Solution):
    @solution
    def totalNQueens(self, n):
        # 28ms 94.78%
        columns = [False] * n
        slash = [False] * (2*n - 1)
        backslash = [False] * (2*n - 1)
        total = [0]

        def dfs(n, i):
            """
            :n: n x n board
            :i: arrange queen in row[i]
            """
            if i == n:
                total[0] += 1
                return
            for j in range(n):
                if columns[j]:
                    continue
                if slash[j-i+n-1] or backslash[i+j]:
                    continue
                columns[j] = True
                slash[j-i+n-1] = True
                backslash[i+j] = True
                dfs(n, i+1)
                backslash[i+j] = False
                slash[j-i+n-1] = False
                columns[j] = False

        dfs(n, 0)
        return total[0]


def main():
    q = Q052()
    q.add_args(4)
    q.add_args(5)
    q.add_args(6)
    q.add_args(7)
    q.run()


if __name__ == "__main__":
    main()
