from leeyzer import Solution, solution


class Q120(Solution):
    @solution
    def minimumTotal(self, triangle):
        # 40ms 89.99%
        if not triangle:
            return 0
        dp = triangle[0]
        for length, row in enumerate(triangle[1:], 2):
            row[0] += dp[0]
            row[-1] += dp[-1]
            for i in range(1, length-1):
                row[i] += min(dp[i-1], dp[i])
            dp = row
        return min(dp)

    @solution
    def min_total(self, triangle):
        # 40ms
        if not triangle:
            return 0
        N = len(triangle)
        dp = [float('inf')] * (N + 2)
        dp[N] = triangle[0][0]

        # [inf, inf, inf, 5, 6, inf]
        # [inf, inf, 11, 10, 13, inf]
        # [inf, 15, 11, 18, 16, inf]

        for i in range(2, N+1):  # this row has i items
            offset = N+1 - i
            for j in range(i):
                # subproblems should avoid being dp[j] and dp[j-1],
                # because dp[j-1] will be overwrited
                dp[offset+j] = triangle[i-1][j] + min(dp[offset+j], dp[offset+j+1])
        return min(dp)


def main():
    q = Q120()
    q.add_args([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]])
    q.run()


if __name__ == "__main__":
    main()
