from leezy import solution, Solution


class Q1335(Solution):
    @solution
    def minDifficulty(self, jobDifficulty, d):
        # 1068 ms, faster than 51.66%
        jobs = jobDifficulty
        INF = float('inf')
        N = len(jobs)
        right_max = [jobs[-1]] * N
        for j in range(N-2, -1, -1):
            right_max[j] = max(jobs[j], right_max[j+1])

        memo = [[None] * (d+1) for _ in range(N)]

        def solve(i, d):
            if N - i < d:
                return INF
            if d == 1:
                return right_max[i]
            if memo[i][d] is not None:
                return memo[i][d]
            ans = INF
            max_ = -1
            for k in range(i, N):
                max_ = max(jobs[k], max_)
                ans = min(ans, max_ + solve(k+1, d-1))
            memo[i][d] = ans
            return ans

        ans = solve(0, d)
        return -1 if ans == INF else ans


def main():
    q = Q1335()
    q.add_case(q.case([6, 5, 4, 3, 2, 1], 2).assert_equal(7))
    q.add_case(q.case([1, 1, 1], 3).assert_equal(3))
    q.add_case(q.case([1, 1, 1], 4).assert_equal(-1))
    q.add_case(q.case([7, 1, 7, 1, 7, 1], 3).assert_equal(15))
    q.add_case(q.case([11, 111, 22, 222, 33, 333, 44, 444], 6).assert_equal(843))
    q.run()


if __name__ == '__main__':
    main()
