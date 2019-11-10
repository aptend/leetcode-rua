from leeyzer import solution, Solution


class Q1254(Solution):
    @solution
    def closedIsland(self, grid):
        # 136ms 100.00%
        m, n = len(grid), len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(i, j):
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 0:
                    grid[ni][nj] = 2
                    dfs(ni, nj)

        for i in range(m):
            for j in [0, n-1]:
                if grid[i][j] == 0:
                    grid[i][j] = 2
                    dfs(i, j)
        for j in range(n):
            for i in [0, m-1]:
                if grid[i][j] == 0:
                    grid[i][j] = 2
                    dfs(i, j)

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    dfs(i, j)
                    ans += 1
        return ans


def main():
    q = Q1254()
    q.add_args([[1, 1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 1, 0], [
               1, 0, 1, 0, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 0]])
    q.run()


if __name__ == '__main__':
    main()
