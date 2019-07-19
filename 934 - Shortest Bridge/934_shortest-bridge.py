from leeyzer import Solution, solution


class Q934(Solution):
    @solution
    def bridge(self, A):
        # 400ms 66.05%
        s1, s2 = set(), set()
        def dfs(i, j):
            if 0 <= i < len(A) and 0 <= j < len(A) and A[i][j] == 1:
                s1.add((i, j))
                A[i][j] = -1
                dfs(i+1, j)
                dfs(i-1, j)
                dfs(i, j-1)
                dfs(i, j+1)
        found = False
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    if not found:
                        dfs(i, j)
                        found = True
                    else:
                        s2.add((i, j))
        seen = s1 | s2
        step = -1
        while s1 and s2:
            step += 1
            if len(s1) > len(s2):
                s1, s2 = s2, s1
            nxt_s = set()
            for i, j in s1:
                for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    ni, nj = i+di, j+dj
                    if (ni, nj) in s2:
                        return step
                    if (ni, nj) in seen:
                        continue
                    seen.add((ni, nj))
                    if not (0 <= ni < len(A) and 0 <= nj < len(A)):
                        continue
                    nxt_s.add((ni, nj))
            s1 = nxt_s
        return -1


    @solution
    def shortestBridge(self, A):
        islands, seen = [], set()
        m, n = len(A), len(A[0])
        for i in range(m):
            for j in range(n):
                if (i, j) not in seen and A[i][j]:
                    current = set()
                    current.add((i, j))
                    seen.add((i, j))
                    self.dfs(A, i, j, current, seen)
                    islands.append(current)

        s1, s2 = islands[:2]
        seen.clear()
        seen |= s1 | s2
        step = -1
        while s1 and s2:
            step += 1
            if len(s1) > len(s2):
                s1, s2 = s2, s1
            nxt_s = set()
            for i, j in s1:
                for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    ni, nj = i+di, j+dj
                    if (ni, nj) in s2:
                        return step
                    if (ni, nj) in seen:
                        continue
                    seen.add((ni, nj))
                    if not (0 <= ni < len(A) and 0 <= nj < len(A)):
                        continue
                    nxt_s.add((ni, nj))
            s1 = nxt_s
        return -1


    def dfs(self, A, i, j, current, seen):
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i+di, j+dj
            if (ni, nj) in seen:
                continue
            seen.add((ni, nj))
            if not (0 <= ni < len(A) and 0 <= nj < len(A[0])):
                continue
            if A[ni][nj]:
                current.add((i, j))
                self.dfs(A, ni, nj, current, seen)




def main():
    q = Q934()
    q.add_args([[0, 1], [1, 0]])
    q.add_args([[0, 1, 0], [0, 0, 0], [0, 0, 1]])
    q.add_args([[1, 1, 1, 1, 1],
                [1, 0, 0, 0, 1],
                [1, 0, 1, 0, 1],
                [1, 0, 0, 0, 1],
                [1, 1, 1, 1, 1]])
    q.add_args([[1, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 1]])
    q.run()


if __name__ == "__main__":
    main()
