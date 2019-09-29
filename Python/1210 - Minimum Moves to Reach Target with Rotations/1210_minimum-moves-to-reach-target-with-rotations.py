from leeyzer import Solution, solution


class Q1210(Solution):
    @solution
    def minimumforwords(self, grid):
        # 732ms inspired by https://leetcode-cn.com/circle/discuss/KzqZdU/view/zFZl1p/
        N = len(grid)
        MAX = float('inf')
        dp = [[[MAX, MAX] for i in range(N)] for j in range(N)]
        dp[0][1][0] = 0

        # actions for a horizontal snake
        def can_forword_h(i, j):
            return j < N-1 and grid[i][j+1] == 0

        def can_rotate(i, j):
            return i < N-1 and j > 0 and grid[i+1][j] == 0 and grid[i+1][j-1] == 0

        def can_merge_v(i, j):
            return i < N-1 and j > 0 and grid[i+1][j-1] == 0 and grid[i+1][j] == 0

        # actions for a vertical snake
        def can_forword_v(i, j):
            return i < N-1 and grid[i+1][j] == 0

        def can_rotate_rev(i, j):
            return j < N-1 and i > 0 and grid[i][j+1] == 0 and grid[i-1][j+1] == 0

        def can_merge_h(i, j):
            return j < N-1 and i > 0 and grid[i-1][j+1] == 0 and grid[i][j+1] == 0

        for i in range(N):
            for j in range(N):
                # consider every possibility to make head at i, j
                if can_forword_h(i, j-1):
                    dp[i][j][0] = min(dp[i][j][0], dp[i][j-1][0]+1)
                if can_merge_v(i-1, j):
                    dp[i][j][0] = min(dp[i][j][0], dp[i-1][j][0]+1)
                if can_forword_v(i, j-1) and can_rotate_rev(i+1, j-1):
                    dp[i][j][0] = min(dp[i][j][0], dp[i][j-1][1]+2)

                if can_forword_v(i-1, j):
                    dp[i][j][1] = min(dp[i][j][1], dp[i-1][j][1]+1)
                if can_merge_h(i, j-1):
                    dp[i][j][1] = min(dp[i][j][1], dp[i][j-1][1]+1)
                # we have determined the value at (i-1, j+1) 
                if j < N -1 and can_rotate(i-1, j+1):
                    dp[i][j][1] = min(dp[i][j][1], dp[i-1][j+1][0]+1)

        ans = dp[N-1][N-1][0]
        return -1 if ans == MAX else ans

    @solution
    def minimum_moves(self, grid):
        # 540ms
        # this is from https://leetcode-cn.com/circle/discuss/KzqZdU/view/zFZl1p/
        N = len(grid)
        MAX = float('inf')
        dp = [[[MAX, MAX] for i in range(N)] for j in range(N)]
        dp[0][1][0] = 0
        for i in range(N):
            for j in range(N):
                # when true, this line tells three things:
                # 0. grid[i][j] = 0, snake can forword here, and
                # 1. graid[i][j-1] = 0, snake can merge down if it is not on 0 row
                # 2. j > 0
                if grid[i][max(0,j-1):min(j+1, N)] == [0, 0]:
                    # forword horiz
                    dp[i][j][0] = min(dp[i][j][0], dp[i][j-1][0]+1)
                    if i > 0: # merge down
                        dp[i][j][0] = min(dp[i][j][0], dp[i-1][j][0]+1)
                    # forword verti and rotate_rev
                    if i < N-1 and j > 0 and grid[i+1][j] == 0 and grid[i+1][j-1] == 0:
                        dp[i][j][0] = min(dp[i][j][0], dp[i][j-1][1]+2)
                
                if [grid[k][j] for k in (max(0, i-1), min(N-1, i))] == [0, 0]:
                    dp[i][j][1] = min(dp[i][j][1], dp[i-1][j][1]+1)
                    if j > 0:
                        dp[i][j][1] = min(dp[i][j][1], dp[i][j-1][1]+1)
                    if j < N-1 and i > 0 and grid[i][j+1] == 0:
                        dp[i][j][1] = min(dp[i][j][1], dp[i-1][j+1][0]+1)
        ans = dp[N-1][N-1][0]
        return -1 if ans == MAX else ans




def main():
    q = Q1210()
    q.add_args([[0, 0, 0, 0, 0, 1],
                [1, 1, 0, 0, 1, 0],
                [0, 0, 0, 0, 1, 1],
                [0, 0, 1, 0, 1, 0],
                [0, 1, 1, 0, 0, 0],
                [0, 1, 1, 0, 0, 0]])
    q.add_args([[0, 0, 1, 1, 1, 1],
                [0, 0, 0, 0, 1, 1],
                [1, 1, 0, 0, 0, 1],
                [1, 1, 1, 0, 0, 1],
                [1, 1, 1, 0, 0, 1],
                [1, 1, 1, 0, 0, 0]])
    q.run()


if __name__ == "__main__":
    main()
