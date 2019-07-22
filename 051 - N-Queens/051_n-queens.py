from leeyzer import Solution, solution


class Q051(Solution):
    @solution
    def solveNQueens(self, n):
        # 40ms 95.29%
        columns = [False] * n
        slash = [False] * (2*n - 1)
        backslash = [False] * (2*n - 1)
        current = [['.']*n for _ in range(n)]
        total = []

        def dfs(n, i):
            """
            :n: n x n board
            :i: arrange queen in row[i]
            """
            if i == n:
                total.append([''.join(r) for r in current])
                return
            for j in range(n):
                if columns[j]:
                    continue
                if slash[j-i+n-1] or backslash[i+j]:
                    continue
                current[i][j] = 'Q'
                columns[j] = True
                slash[j-i+n-1] = True
                backslash[i+j] = True
                dfs(n, i+1)
                backslash[i+j] = False
                slash[j-i+n-1] = False
                columns[j] = False
                current[i][j] = '.'

        dfs(n, 0)
        return total


def main():
    q = Q051()
    q.add_args(5)
    q.run()


if __name__ == "__main__":
    main()
