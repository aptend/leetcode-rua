from leezy import solution, Solution


class Q132(Solution):
    @solution
    def minCut(self, s):
        # 484ms 54.89%
        N = len(s)
        is_palin = [[True] * N for _ in range(N)]
        for l in range(2, N+1):
            for i in range(N-l+1):
                j = i + l - 1
                is_palin[i][j] = s[i] == s[j] and is_palin[i+1][j-1]
        # min cuts using s[..=i]
        dp = [float('inf')] * N
        for i in range(N):
            if is_palin[0][i]:
                dp[i] = 0
                continue
            for j in range(1, i+1):
                if is_palin[j][i]:
                    dp[i] = min(dp[i], dp[j-1] + 1)
        return dp[N-1]


def main():
    q = Q132()
    q.add_case(q.case('aab').assert_equal(1))
    q.add_case(q.case('aaa').assert_equal(0))
    q.run()


if __name__ == '__main__':
    main()
