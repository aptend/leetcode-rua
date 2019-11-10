from leezy import Solution, solution


class Q827(Solution):
    @solution
    def largestIsland(self, grid):
        # 88ms 99.31%
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        boundry = [0] * (n * m)
        contour = set()

        def dfs(i, j):
            if not (0 <= i < m and 0 <= j < n):
                return 0
            if grid[i][j] == 0:
                contour.add(i*m+j)  # record island's contour
                return 0
            if grid[i][j] == 2:
                return 0
            grid[i][j] = 2  # 2 means we have visited this point
            return 1 + dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1)

        max_island = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = dfs(i, j)
                    max_island = max(max_island, area)
                    for idx in contour:
                        boundry[idx] += area
                    contour.clear()
        return max(max_island, max(boundry)+1)



def main():
    q = Q827()
    q.add_args([[1, 0], [0, 1]])
    q.add_args([[1, 1], [0, 1]])
    q.add_args([[1, 1], [1, 1]])
    q.run()


if __name__ == "__main__":
    main()
