from leeyzer import Solution, solution


class Q04(Solution):
    @solution
    def domino(self, n, m, broken):
        # brute TLE 11/94
        brd = [[0] * m for _ in range(n)]
        for x, y in broken:
            brd[x][y] = -1

        dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        self.g_max = 0

        def place(cnt):
            found = False
            for i in range(n):
                for j in range(m):
                    if brd[i][j] == 0:
                        for di, dj in dirs:
                            ni, nj = i + di, j + dj
                            if 0 <= ni < n and 0 <= nj < m and brd[ni][nj] == 0:
                                found = True
                                brd[i][j] = -1
                                brd[ni][nj] = -1
                                place(cnt+1)
                                brd[i][j] = 0
                                brd[ni][nj] = 0
            if not found:
                self.g_max = max(self.g_max, cnt)
        place(0)
        return self.g_max

    @solution
    def do(self, n, m, broken):
        # solution from https://leetcode-cn.com/u/sleepybag/
        # greedy solution. i don't know how to prove it
        b = [[0 for i in range(m + 2)] for j in range(n + 2)]
        for x, y in broken:
            b[x + 1][y + 1] = 1
        for x in range(0, n + 2):
            b[x][0] = 1
            b[x][-1] = 1
        for y in range(0, m + 2):
            b[0][y] = 1
            b[-1][y] = 1

        def corner(x, y):
            d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            c = 0
            for dx, dy in d:
                if b[x + dx][y + dy]:
                    c += 1
            return c

        def put(x, y):
            b[x][y] = 1
            d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for dx, dy in d:
                if not b[x + dx][y + dy]:
                    b[x + dx][y + dy] = 1
                    break
            return

        ans = 0
        go_on = True
        while go_on:
            go_on = False
            for x in range(n):
                for y in range(m):
                    if not b[x + 1][y + 1]:
                        c = corner(x + 1, y + 1)
                        # dead grid, fill it
                        if c == 4:
                            b[x + 1][y + 1] = 1
                            go_on = True
                        # only one way to place domino, fill it
                        elif c == 3:
                            put(x + 1, y + 1)
                            ans += 1
                            go_on = True

            # don't find top-priority grid, make one here
            if not go_on:
                for x in range(n):
                    for y in range(m):
                        if not go_on and not b[x + 1][y + 1]:
                            c = corner(x + 1, y + 1)
                            if c == 2 or c == 1:
                                put(x + 1, y + 1)
                                ans += 1
                                go_on = True

        return ans




def main():
    q = Q04()
    q.add_args(2, 3, [[1, 0], [1, 1]])
    q.add_args(3, 3, [])
    q.run()


if __name__ == "__main__":
    main()
