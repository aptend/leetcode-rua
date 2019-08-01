from leeyzer import Solution, solution
from collections import deque


class Q542(Solution):
    @solution
    def updateMatrix(self, matrix):
        # 500ms 95.21%
        MAX = float('inf')
        m, n = len(matrix), len(matrix[0])
        ans = [[MAX]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if matrix[i][j]:
                    if i > 0:
                        ans[i][j] = min(ans[i][j], ans[i-1][j]+1)
                    if j > 0:
                        ans[i][j] = min(ans[i][j], ans[i][j-1]+1)
                else:
                    ans[i][j] = 0

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if matrix[i][j]:
                    if i < m-1:
                        ans[i][j] = min(ans[i][j], ans[i+1][j]+1)
                    if j < n-1:
                        ans[i][j] = min(ans[i][j], ans[i][j+1]+1)
        return ans

    @solution
    def update_matrix(self, matrix):
        # 632ms 64.04%
        m, n = len(matrix), len(matrix[0])
        q = deque()
        seen = set()
        ans = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    q.append((i, j))
                    seen.add((i, j))
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        steps = 0
        while q:
            steps += 1
            for _ in range(len(q)):
                i, j = q.popleft()
                for di, dj in directions:
                    ni, nj = i+di, j+dj
                    if (ni, nj) in seen:
                        continue
                    if not (0 <= ni < m and 0 <= nj < n):
                        continue
                    seen.add((ni, nj))
                    q.append((ni, nj))
                    ans[ni][nj] = steps
        return ans


def main():
    q = Q542()
    q.add_args([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
    q.add_args(
        [[0, 0, 0],
         [0, 1, 0],
         [1, 1, 1]]
    )
    q.run()


if __name__ == "__main__":
    main()
