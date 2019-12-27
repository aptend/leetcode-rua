from leezy import solution, Solution
from collections import deque

class Q1091(Solution):
    @solution
    def shortestPathBinaryMatrix(self, grid):
        # 692ms 68.02%
        m, n = len(grid), len(grid[0])
        if grid[0][0] == 1:
            return -1
        q = deque()
        q.append((0, 0))
        step = 0
        dirs = [(1, 0), (1, -1), (1, 1), (0, 1), (0, -1), (-1, 0), (-1, -1), (-1, 1)]
        seen = set()
        while q:
            step += 1
            for _ in range(len(q)):
                i, j = q.popleft()
                if i == m-1 and j == n-1:
                    return step
                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if not (0 <= ni < m and 0 <= nj < n):
                        continue
                    if grid[ni][nj] == 1 or (ni, nj) in seen:
                        continue
                    seen.add((ni, nj))
                    q.append((ni, nj))
        return -1


def main():
    q = Q1091()
    q.add_case(q.case([[0, 1], [1, 0]]).assert_equal(2))
    q.add_case(q.case([[0, 0, 0], [1, 1, 0], [1, 1, 0]]).assert_equal(4))
    q.run()

if __name__ == '__main__':
    main()
