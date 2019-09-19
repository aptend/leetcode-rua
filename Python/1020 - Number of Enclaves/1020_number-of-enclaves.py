from leeyzer import Solution, solution


class Q1020(Solution):
    @solution
    def numEnclaves(self, A):
        # 592ms 71.16%
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m, n = len(A), len(A[0])

        def dfs(i, j):
            A[i][j] = -1
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < m and 0 <= nj < n and A[ni][nj] == 1:
                    dfs(ni, nj)
        for i in range(m):
            for j in (0, n-1):
                if A[i][j] == 1:
                    dfs(i, j)
        for j in range(n):
            for i in (0, m-1):
                if A[i][j] == 1:
                    dfs(i, j)
        ans = 0
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    ans += 1
        return ans
    


def main():
    q = Q1020()
    q.add_args([[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]])
    q.add_args([[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]])
    q.run()


if __name__ == "__main__":
    main()
