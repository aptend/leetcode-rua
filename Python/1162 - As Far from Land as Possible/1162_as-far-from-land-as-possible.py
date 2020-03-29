from leezy import solution, Solution
from collections import deque


class Q1162(Solution):
    @solution
    def maxDistance(self, grid):
        q = deque()
        N = len(grid)
        seen = set()
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 1:
                    seen.add((i, j))
                    q.append((i, j))
        step = -1
        while q:
            step += 1
            for _ in range(len(q)):
                i, j = q.popleft()
                for di, dj in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    ni, nj = i + di, j + dj
                    if not (0 <= ni < N and 0 <= nj < N):
                        continue
                    if grid[ni][nj] == 1 or (ni, nj) in seen:
                        continue
                    seen.add((ni, nj))
                    q.append((ni, nj))
        return -1 if step <= 0 else step


def main():
    q = Q1162()
    q.add_case(q.case([[1, 0, 1], [0, 0, 0], [1, 0, 1]]).assert_equal(2))
    q.add_case(q.case([[0, 0, 0], [0, 0, 0], [0, 0, 0]]).assert_equal(-1))
    q.add_case(q.case([[1, 1, 1], [1, 1, 1], [1, 1, 1]]).assert_equal(-1))
    q.add_case(q.case([[1, 0, 0], [0, 0, 0], [0, 0, 0]]).assert_equal(4))
    q.run()


if __name__ == '__main__':
    main()
