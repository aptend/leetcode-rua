from leezy import solution, Solution
from collections import deque


class Q994(Solution):
    @solution
    def orangesRotting(self, grid):
        # 48ms 95.89%
        q = deque()
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        step = 0
        while q:
            found = False
            for _ in range(len(q)):
                i, j = q.popleft()
                for di, dj in dirs:
                    ni, nj = di + i, dj + j
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                        q.append((ni, nj))
                        grid[ni][nj] = 2
                        found = True
            if found:
                step += 1
        for row in grid:
            for x in row:
                if x == 1:
                    return -1
        return step


def main():
    q = Q994()
    q.add_case(q.case([[2, 1, 1], [1, 1, 0], [0, 1, 1]]).assert_equal(4))
    q.add_case(q.case([[2, 1, 1], [1, 1, 0], [1, 0, 1]]).assert_equal(-1))
    q.add_case(q.case([[2, 0]]).assert_equal(0))
    q.run()


if __name__ == '__main__':
    main()
