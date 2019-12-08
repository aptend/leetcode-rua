from leezy import solution, Solution


class Q329(Solution):
    @solution
    def longestIncreasingPath(self, matrix):
        # 472ms 79.91%
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        memo = [[0] * n for _ in range(m)]
        dis = [1, 0, -1, 0]
        djs = [0, 1, 0, -1]
        def dfs(i, j):
            if memo[i][j]:
                return memo[i][j]
            ans = 1
            for di, dj in zip(dis, djs):
                ni, nj = i + di, j + dj
                if not (0 <= ni < m and 0 <= nj < n):
                    continue
                if matrix[ni][nj] < matrix[i][j]:
                    ans = max(ans, dfs(ni, nj) + 1)
            memo[i][j] = ans
            return ans
        return max((dfs(i, j) for i in range(m) for j in range(n)), default=0)



def main():
    q = Q329()
    q.add_case(q.case([[9, 9, 4], [6, 6, 8], [2, 1, 1]]).assert_equal(4))
    q.add_case(q.case([[3, 4, 5], [3, 2, 6], [2, 2, 1]]).assert_equal(4))
    q.add_case(q.case([[]]).assert_equal(0))
    q.add_case(q.case([[1]]).assert_equal(1))
    q.run()


if __name__ == '__main__':
    main()
