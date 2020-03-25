from leezy import solution, Solution


class Q892(Solution):
    @solution
    def surfaceArea(self, grid):
        ans = 0
        N = len(grid)
        for i in range(N):
            for j in range(N):
                x = grid[i][j]
                ans += 6 + 4 * (x-1) if x > 0 else 0
                if i > 0:
                    ans -= min(x, grid[i-1][j])
                if i < N-1:
                    ans -= min(x, grid[i+1][j])
                if j > 0:
                    ans -= min(x, grid[i][j-1])
                if j < N-1:
                    ans -= min(x, grid[i][j+1])
        return ans


def main():
    q = Q892()
    q.add_case(q.case([[2]]).assert_equal(10))
    q.add_case(q.case([[1, 2], [3, 4]]).assert_equal(34))
    q.add_case(q.case([[1, 0], [0, 2]]).assert_equal(16))
    q.add_case(q.case([[1, 1, 1], [1, 0, 1], [1, 1, 1]]).assert_equal(32))
    q.add_case(q.case([[2, 2, 2], [2, 1, 2], [2, 2, 2]]).assert_equal(46))
    q.run()


if __name__ == '__main__':
    main()
