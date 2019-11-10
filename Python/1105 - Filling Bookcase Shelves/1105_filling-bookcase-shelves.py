from leezy import Solution, solution


class Q1105(Solution):
    @solution
    def minHeightShelves(self, books, shelf_width):
        # 40ms 50.20%
        N, MAX = len(books), float('inf')
        # dp[i] means min height after placing books[:i]
        dp = [MAX] * (N+1)
        dp[0] = 0
        for i in range(1, N+1):
            w, h = 0, 0
            # the last n books are placed on the same level
            for n in range(1, i+1):
                w += books[i-n][0]
                if w > shelf_width:
                    break
                h = max(h, books[i-n][1])
                dp[i] = min(dp[i], dp[i-n]+h)
        return dp[N]


    @solution
    def min_height(self, books, shelf_width):
        # 最初的想法，dp[i][j]前i本书，占最后一层j个单位
        # dp[i][j][0] 最后一层的最大高度
        # dp[i][j][1] 此时的总高度
        # dp[i][0][1] 用了i本书后最小总高度
        MAX = float('inf')
        N = len(books)
        dp = [[[MAX, MAX] for _ in range(shelf_width+1)] for _ in range(N+1)]
        dp[0][0] = [0, 0]
        for i in range(1, N+1):
            # 单独放一层
            w, h = books[i-1]
            dp[i][w][0] = h  # 当前层的最大高度
            dp[i][w][1] = dp[i-1][0][1] + h  # 迄今为止的最小总高
            min_total = dp[i][w][1]
            for j in range(w+1, shelf_width+1):
                player_h, ptotal_h = dp[i-1][j-w]
                if player_h == MAX:
                    continue
                if h > player_h:
                    dp[i][j][0] = h
                    dp[i][j][1] = ptotal_h + h - player_h
                else:
                    dp[i][j][0] = player_h
                    dp[i][j][1] = ptotal_h
                min_total = min(min_total, dp[i][j][1])
            dp[i][0][1] = min_total
        return dp[N][0][1]





def main():
    q = Q1105()
    q.add_args([[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]], 4)
    q.run()


if __name__ == "__main__":
    main()
