from leezy import Solution, solution

class Q688(Solution):
    @solution
    def knightProbability(self, N, K, r, c):
        # 128ms 93.33%
        directions = [
            (1, 2), (1, -2), (-1, 2), (-1, -2),
            (2, 1), (2, -1), (-2, 1), (-2, -1),
        ]
        dp = [[0]*N for _ in range(N)]
        cur_dp = [[0]*N for _ in range(N)]
        dp[r][c] = 1
        for _ in range(K):
            print(cur_dp)
            for i in range(N):
                for j in range(N):
                    if dp[i][j] == 0:
                        continue
                    for di, dj in directions:
                        ni, nj = i+di, j+dj
                        if 0 <= ni < N and 0 <= nj < N:
                            cur_dp[ni][nj] += dp[i][j]
            cur_dp, dp = dp, cur_dp
            print(dp)
            for row in cur_dp:
                for i in range(N):
                    row[i] = 0
        cnt = 0
        for row in dp:
            for x in row:
                cnt += x
        return cnt / (8**K)



def main():
    q = Q688()
    q.add_args(3, 2, 0, 0)
    q.run()


if __name__ == "__main__":
    main()
