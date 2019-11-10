from leezy import solution, Solution

class Q1034(Solution):
    @solution
    def colorBorder(self, grid, r0, c0, color):
        # 152ms 87.36%
        M, N = len(grid), len(grid[0])
        old_c = grid[r0][c0]
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(i, j, border):
            is_border_cell = False
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if not (0 <= ni < M and 0 <= nj < N):
                    is_border_cell = True
                    continue
                if grid[ni][nj] != old_c:
                    if grid[ni][nj] != -1:
                        is_border_cell = True
                    continue
                grid[i][j] = -1
                dfs(ni, nj, border)
                grid[i][j] = old_c
            if is_border_cell:
                border.append((i, j))
        border = []
        dfs(r0, c0, border)
        for i, j in border:
            grid[i][j] = color
        return grid


def main():
    q = Q1034()
    q.add_args([[1, 1], [1, 2]], 0, 0, 3)
    q.run()

if __name__ == '__main__':
    main()
