from leeyzer import Solution, solution


class Q695(Solution):
    @solution
    def maxAreaOfIsland(self, grid):
        # 116ms 82.51%
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        def dfs(i, j):
            if not (0 <= i < m and 0 <= j < n):
                return 0
            if grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            return 1 + dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1)

        g_max = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    g_max = max(g_max, dfs(i, j))
        return g_max


def main():
    q = Q695()
    q.add_args([[0, 0, 0, 0, 0]])
    q.add_args([[1, 1, 0, 0, 0],
                [1, 1, 0, 0, 0],
                [0, 0, 0, 1, 1],
                [0, 0, 0, 1, 1]])
    q.add_args([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]])
    q.run()


if __name__ == "__main__":
    main()
