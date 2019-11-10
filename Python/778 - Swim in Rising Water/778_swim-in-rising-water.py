from leezy import Solution, solution

from collections import deque
class Q778(Solution):
    @solution
    def swimInWater(self, grid):
        N = len(grid)
        directions = [(1,0), (-1,0), (0, 1), (0, -1)]
        def dfs_can_pass_at_time(t):
            # 132ms 40.82%
            def dfs(i, j):
                if i == N-1 and j == N-1:
                    return True
                for di, dj in directions:
                    ni, nj = i+di, j+dj
                    if not (0 <= ni < N and 0 <= nj < N):
                        continue
                    if grid[ni][nj] > t or (ni, nj) in seen:
                        continue
                    seen.add((ni, nj))
                    if dfs(ni, nj):
                        return True
                return False
            seen = set()
            if grid[0][0] > t:
                return False
            seen.add((0, 0))
            return dfs(0, 0)

        def bfs_can_pass_at_time(t):
            # 224ms 17.86%
            if grid[0][0] > t:
                return False
            queue = deque()
            queue.append((0, 0))
            seen = set()
            seen.add((0, 0))
            while queue:
                for _ in range(len(queue)):
                    i, j = queue.popleft()
                    for di, dj in directions:
                        ni, nj = i+di, j+dj
                        if not (0 <= ni < N and 0 <= nj < N):
                            continue
                        if grid[ni][nj] > t or (ni, nj) in seen:
                            continue
                        if ni == N-1 and nj == N-1:
                            return True
                        seen.add((ni, nj))
                        queue.append((ni, nj))

        lo, hi = 0, N*N-1
        while lo <= hi:
            m = lo + (hi - lo) // 2
            # if bfs_can_pass_at_time(m):
            if dfs_can_pass_at_time(m):
                hi = m - 1
            else:
                lo = m + 1
        return lo


def main():
    q = Q778()
    q.add_args([[0, 2], [1, 3]])
    q.add_args([[3, 2], [1, 0]])
    q.add_args([[0, 1, 2, 3, 4],
                [24, 23, 22, 21, 5],
                [12, 13, 14, 15, 16],
                [11, 17, 18, 19, 20],
                [10, 9, 8, 7, 6]])
    q.add_args(
        [[7, 34, 16, 12, 15, 0],
         [10, 26, 4, 30, 1, 20],
         [28, 27, 33, 35, 3, 8],
         [29, 9, 13, 14, 11, 32],
         [31, 21, 23, 24, 19, 18],
         [22, 6, 17, 5, 2, 25]])
    q.run()


if __name__ == "__main__":
    main()
