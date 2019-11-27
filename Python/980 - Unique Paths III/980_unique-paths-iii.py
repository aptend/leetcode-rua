from leezy import solution, Solution


class Q980(Solution):
    @solution
    def uniquePathsIII(self, grid):
        # 60ms 79.97%
        m, n = len(grid), len(grid[0])
        z_cnt = 0
        si = sj = 0
        for i in range(m):
            for j in range(n):
                x = grid[i][j]
                if x == 0:
                    z_cnt += 1
                elif x == 1:
                    si, sj = i, j
        self.ans = 0

        def dfs(i, j, z):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            x = grid[i][j]
            if x == -1:
                return
            if x == 2:
                if z == 0:
                    self.ans += 1
                return
            grid[i][j] = -1
            dfs(i+1, j, z-1)
            dfs(i-1, j, z-1)
            dfs(i, j+1, z-1)
            dfs(i, j-1, z-1)
            grid[i][j] = x

        dfs(si, sj, z_cnt+1)
        return self.ans


def main():
    q = Q980()
    q.add_case(q.case([[1, 0, 0, 0],
                       [0, 0, 0, 0],
                       [0, 0, 2, -1]]).assert_equal(2))
    q.add_case(q.case([[1, 0, 0, 0],
                       [0, 0, 0, 0],
                       [0, 0, 0, 2]]).assert_equal(4))
    q.run()

if __name__ == '__main__':
    main()
