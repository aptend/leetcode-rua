from leezy import solution, Solution


class Q1575(Solution):
    @solution
    def countRoutes(self, x, start, finish, F):
        # 2076 ms faster than 90.14%
        k_mod = 10**9 + 7
        N = len(x)
        dp = [[0 for _ in range(F+1)] for _ in range(N)]
        dp[start][F] = 1
        for f in range(F, -1, -1):
            for p in range(N):
                if dp[p][f] == 0 or abs(x[p] - x[finish]) > f:
                    continue
                for np in range(N):
                    delta = abs(x[p] - x[np])
                    if np == p or delta > f:
                        continue
                    dp[np][f-delta] = (dp[np][f-delta] + dp[p][f]) % k_mod

        return sum(dp[finish][f] for f in range(F+1)) % k_mod


def main():
    q = Q1575()
    q.add_case(q.case([2, 3, 6, 8, 4], 1, 3, 5).assert_equal(4))
    q.add_case(q.case([1, 2, 3], 0, 2, 40).assert_equal(615088286))
    q.add_case(q.case([4, 3, 1], 1, 0, 6).assert_equal(5))
    q.run()


if __name__ == '__main__':
    main()
