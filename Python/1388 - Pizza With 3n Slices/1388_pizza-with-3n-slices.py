from leezy import solution, Solution


class Q1388(Solution):
    @solution
    def maxSizeSlices(self, slices):
        # 244 ms faster than 80.00%
        K = len(slices) // 3
        def max_size_inner(slices):
            N = len(slices)
            dp = [[0]*(K+1) for _ in range(N+1)]
            dp[1][1] = slices[0]
            for i in range(2, N+1):
                # given i numbers, we pick at most i//2 + 1 no-adjcent numbers
                for j in range(1, min(i//2+1, K)+1):
                    dp[i][j] = max(
                        dp[i-1][j],
                        dp[i-2][j-1] + slices[i-1]
                    )
            return dp[N][K]
        return max(max_size_inner(slices[1:]), max_size_inner(slices[:-1]))



def main():
    q = Q1388()
    q.add_case(q.case([1, 2, 3, 4, 5, 6]).assert_equal(10))
    q.add_case(q.case([8, 9, 8, 6, 1, 1]).assert_equal(16))
    q.add_case(q.case([4, 1, 2, 5, 8, 3, 1, 9, 7]).assert_equal(21))
    q.add_case(q.case([1, 2, 3]).assert_equal(3))
    q.run()


if __name__ == '__main__':
    main()
