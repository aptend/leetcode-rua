from leeyzer import Solution, solution


class Q200(Solution):
    @solution
    def numIslands(self, grid):
        # 124ms 80.47%
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        seen = [[False] * n for _ in range(m)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(i, j):
            seen[i][j] = True
            for di, dj in directions:
                ni, nj = i+di, j+dj
                if not (0 <= ni < m and 0 <= nj < n):
                    continue
                if not seen[ni][nj] and grid[ni][nj] == '1':
                    dfs(ni, nj)
        cc_count = 0
        for i in range(m):
            for j in range(n):
                if not seen[i][j] and grid[i][j] == '1':
                    dfs(i, j)
                    cc_count += 1
        return cc_count

    @solution
    def nums_islands(self, grid):
        # 120ms 86.24%  / 124ms
        # do not use seen and handle out of boundray at the beginning
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if not (0 <= i < m and 0 <= j < n):
                return
            if grid[i][j] == '0':
                return
            grid[i][j] = '0'  # turn 1 to 0, which means we have visted it
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        cc_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    cc_count += 1
        return cc_count



def main():
    q = Q200()
    q.add_args([['1', '1', '1', '1', '0'],
                ['1', '1', '0', '1', '0'],
                ['1', '1', '0', '0', '0'],
                ['0', '0', '0', '0', '0']])

    q.add_args([['1', '1', '0', '0', '0'],
                ['1', '1', '0', '0', '0'],
                ['0', '0', '1', '0', '0'],
                ['0', '0', '0', '1', '1']])
    q.run()


if __name__ == "__main__":
    main()
