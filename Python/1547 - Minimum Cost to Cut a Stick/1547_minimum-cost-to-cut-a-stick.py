from leezy import solution, Solution


class Q1547(Solution):
    @solution
    def minCost(self, n, cuts):
        # 520 ms faster than 98.19%
        # convert this problem to 1000-merge stones with K = 2
        cuts = sorted(cuts) + [n]
        stones = [cuts[0]] + [r-p for r, p in zip(cuts[1:], cuts)]
        p_sum = [0]
        for s in stones:
            p_sum.append(p_sum[-1] + s)
        N = len(stones)
        # dp[i][j] means minimum cost to merge ith to jth(inclusive) stones
        # gap=0 case, dp[i][i] = 0
        dp = [[0] * N for _ in range(N)]
        for gap in range(1, N):
            for i in range(0, N-gap):
                j = i + gap
                opt = min(dp[i][k] + dp[k+1][j] for k in range(i, j))
                dp[i][j] = p_sum[j+1] - p_sum[i] + opt
        return dp[0][N-1]


def main():
    q = Q1547()
    q.add_case(q.case(7, [1, 3, 4, 5]))
    q.add_case(q.case(9, [5, 6, 1, 4, 2]))
    q.run()


if __name__ == '__main__':
    main()
