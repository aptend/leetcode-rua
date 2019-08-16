from leeyzer import Solution, solution


class Q576(Solution):
    @solution
    def findPaths(self, m, n, N, i, j):
        # 104ms 94.24% / 100ms
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # dp[i][j] means how many ways to reach (i, j) after k steps
        dp = [[0] * n for _ in range(m)]
        cur_dp = [[0] * n for _ in range(m)]
        dp[i][j] = 1
        ans = 0
        kmod = 10**9 + 7
        for _ in range(N):
            for i in range(m):
                for j in range(n):
                    if dp[i][j] == 0:
                        continue
                    for di, dj in directions:
                        ni, nj = i+di, j+dj
                        if 0 <= ni < m and 0 <= nj < n:
                            cur_dp[ni][nj] += dp[i][j]
                        else:
                            # still be risky to overflow
                            ans = (ans + dp[i][j]) % kmod
            cur_dp, dp = dp, cur_dp
            for row in cur_dp:
                for k in range(n):
                    row[k] = 0
        return int(ans)
    
    @solution
    def find_paths(self, m, n, N, i, j):
        # 336ms 24.69%
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        dp = [[0] * n for _ in range(m)]
        # dp[i][j] means how many ways from out of boundry to (i, j) after k steps
        cur_dp = [[0] * n for _ in range(m)]
        kmod = 10**9 + 7
        I, J = i, j
        for _ in range(N):
            for i in range(m):
                for j in range(n):
                    for di, dj in directions:
                        ni, nj = i+di, j+dj
                        if 0 <= ni < m and 0 <= nj < n:
                            cur_dp[i][j] = (cur_dp[i][j] + dp[ni][nj]) % kmod
                        else:
                            cur_dp[i][j] += 1
            cur_dp, dp = dp, cur_dp
            for row in cur_dp:
                for k in range(n):
                    row[k] = 0
        return dp[I][J]

def main():
    q = Q576()
    q.add_args(2, 2, 2, 0, 0)
    q.add_args(2, 2, 40, 0, 0) # 23240157
    q.add_args(1, 3, 3, 0, 1)
    q.add_args(1, 3, 30, 0, 1)
    q.run()


if __name__ == "__main__":
    main()
 
