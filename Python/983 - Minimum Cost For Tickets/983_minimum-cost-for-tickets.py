from leeyzer import Solution, solution


class Q983(Solution):
    @solution
    def mincostTickets(self, days, costs):
        dp = [0] * 366
        for d in days:
            dp[d] = 1
        for i in range(1, 366):
            if dp[i] == 0:
                dp[i] = dp[i-1]
            else:
                dp[i] = min(dp[i-1] + costs[0],
                            dp[max(0, i-7)] + costs[1],
                            dp[max(0, i-30)] + costs[2])
        return dp[365]


def main():
    q = Q983()
    q.add_args([1, 4, 6, 7, 8, 20], [2, 7, 15])  # 11
    q.add_args([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31]
               , [2, 7, 15])  # 17
    q.add_args([1, 2, 3, 4, 6, 8, 9, 10, 13, 14,
                16, 17, 19, 21, 24, 26, 27, 28, 29],
                [3, 14, 50])
    q.run()


if __name__ == "__main__":
    main()
