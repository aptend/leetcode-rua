from leezy import solution, Solution


class Q1402(Solution):
    @solution
    def maxSatisfaction(self, satisfaction):
        S = sorted(satisfaction)
        N = len(S)
        memo = [[None]*(N+1) for _ in range(N+1)]

        def solve(i, j):
            if j == 0:
                return 0
            if i == 0 or i < j:
                return float('-inf')
            if memo[i][j] is not None:
                return memo[i][j]
            ans = max(solve(i-1, j), solve(i-1, j-1) + S[i-1]*j)
            memo[i][j] = ans
            return ans

        return max(solve(N, j) for j in range(N+1))

    @solution
    def max_stat(self, S):
        S = sorted(S)
        N = len(S)
        dp = [0] + [float('-inf')] * N
        new_dp = dp[:]
        for i, s in enumerate(S, 1):
            for j in range(1, i+1):
                new_dp[j] = max(dp[j], dp[j-1] + s * j)
            dp, new_dp = new_dp, dp
        return max(dp)
    
    @solution
    def max_greedy(self, S):
        # we would like to assign the higher satisfaction level dish with a higher weight.
        # it's natural to sort the array, but when to stop? 
        # How many dishes do we need to maximize `like-time`?
        # [-9, -8, -1, 0, 5]
        # let's say we have [0, 5] and the like-time is 0*1 + 5*2
        # it's profitable to cook -1? yes, because the delta is 0 + 5 - 1
        # we will do unitl delta < 0
        S = sorted(S, reverse=True)
        acc_delta = 0
        ans = 0
        for s in S:
            acc_delta += s
            if acc_delta < 0:
                break
            ans += acc_delta
        return ans




def main():
    q = Q1402()
    q.add_case(q.case([-1, -8, 0, 5, -7]).assert_equal(14))
    q.add_case(q.case([4, 3, 2]).assert_equal(20))
    q.add_case(q.case([-1, -4, -5]).assert_equal(0))
    q.add_case(q.case([-2, 5, -1, 0, 3, -3]).assert_equal(35))
    q.run()


if __name__ == '__main__':
    main()
