from leezy import Solution, solution


class Q1219(Solution):
    @solution
    def getMaximumGold(self, grid):
        # 1380ms 64.03%
        m, n = len(grid), len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        self.g_max = 0
        def dfs(i, j, amount):
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] != 0:
                    tmp = grid[ni][nj]
                    grid[ni][nj] = 0
                    dfs(ni, nj, amount + tmp)
                    grid[ni][nj] = tmp
                else:
                    self.g_max = max(self.g_max, amount)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    tmp = grid[i][j]
                    grid[i][j] = 0
                    dfs(i, j, tmp)
                    grid[i][j] = tmp
        return self.g_max


def main():
    q = Q1219()
    q.add_args([[0, 6, 0], [5, 8, 7], [0, 9, 0]])
    q.run()


if __name__ == "__main__":
    main()
