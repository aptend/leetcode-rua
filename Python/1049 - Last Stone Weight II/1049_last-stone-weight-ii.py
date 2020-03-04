from leezy import solution, Solution


class Q1049(Solution):
    @solution
    def lastStoneWeightII(self, stones):
        # 36 ms, 81.10%
        N = sum(stones) // 2
        dp = [False] * (N+1)
        dp[0] = True
        for x in stones:
            for j in range(N, x-1, -1):
                dp[j] |= dp[j-x]
        i = 0
        while i < N+1 and not dp[N-i]:
            i += 1
        return sum(stones) - 2*(N-i)


def main():
    q = Q1049()
    q.add_case(q.case([2, 7, 4, 1, 8, 1]).assert_equal(1))
    q.add_case(q.case([8, 4, 4]).assert_equal(0))
    q.add_case(q.case([8, 1]).assert_equal(7))
    q.add_case(q.case([3]).assert_equal(3))
    q.run()


if __name__ == '__main__':
    main()
